import asyncio
from fastapi import APIRouter
from app.model.task_manager import send_sms
from redis import Redis
from rq import Queue
from app.model.sms import SMSSchema
from starlette.responses import JSONResponse

sms = APIRouter()
q = Queue(connection=Redis())


@sms.post('/v1/send')
async def handle_form(sms:SMSSchema):
	q.enqueue(send_sms, sms)
	return JSONResponse(status_code=200, content={"message": "sms has been sent"})
