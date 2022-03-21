# import os
import json
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .email import EmailSchema
# from dotenv import load_dotenv
from pathlib import Path
from twilio.rest import Client
from app.config import get_settings
from app.conn.user_devices import UserDevice
from app.conn import db_manager
from app.model.push import ErrorResponse, UserDevicePayload, MessagePayload, Response
from fastapi import HTTPException
from typing import List, Mapping, Dict
from app.clients.fcm import fcm
from starlette.responses import JSONResponse
from redis import Redis
from rq import Queue
from app.model.sms import SMSSchema

q = Queue(connection=Redis())

settings = get_settings()



conf = ConnectionConfig(
	MAIL_USERNAME=settings.MAIL_USERNAME,
	MAIL_PASSWORD=settings.MAIL_PASSWORD,
	MAIL_FROM=settings.MAIL_FROM,
	MAIL_PORT=settings.MAIL_PORT,
	MAIL_SERVER=settings.MAIL_SERVER,
	MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
	MAIL_TLS=True,
	MAIL_SSL=False,
	USE_CREDENTIALS=True,
	TEMPLATE_FOLDER=Path(__file__).parent.parent / 'templates/email',
)


async def send_email_task(email: EmailSchema):

	message = MessageSchema(
		subject=email.dict().get("subject"),
		recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
		template_body=email.dict().get("body"),
		)

	fm = FastMail(conf)
	await fm.send_message(message, template_name="email.html")
	return JSONResponse(status_code=200, content={"message": "email has been sent"})     


def send_email_background_task(background_tasks: BackgroundTasks, email:EmailSchema):
	message = MessageSchema(
		subject=email.dict().get("subject"),
		recipients=email.dict().get("email"), 
		template_body=email.dict().get("body"),
	)

	fm = FastMail(conf)

	background_tasks.add_task(
		fm.send_message, message, template_name='email.html')
def send_sms(sms:SMSSchema):
	client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	return client.messages.create(from_=settings.TWILIO_PHONE_NUMBER,
								  to=sms.phone, body=sms.body)

async def save_push_notification_user_data(db, user_device: UserDevicePayload) -> Dict:
	last_record_id = await db_manager.save(db, user_device)
	return last_record_id


async def get_tokens(db,user_id) -> List[Mapping]:
	tokens = await db_manager.get_tokens(db, user_id)

	return tokens


async def send_push_notification(message: MessagePayload,db):
	tokens = await get_tokens(db,message.user_id)
	converted_tokens = [value.token for value in tokens]

	if len(converted_tokens) == 0:
		raise HTTPException(status_code=404,
							detail=f'user id {message.user_id} don\'t have any registered device(s)')
	q.enqueue(fcm.send, message.notify.title,message.notify.body,converted_tokens)

	return JSONResponse(status_code=200, content={"message": "message has been sent"})
