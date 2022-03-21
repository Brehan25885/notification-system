from fastapi import APIRouter,BackgroundTasks
from app.model.task_manager import send_email_task,send_email_background_task
from app.model.email import EmailSchema
from starlette.responses import JSONResponse
from redis import Redis
from rq import Queue

notify = APIRouter()
q = Queue(connection=Redis())

@notify.post("/v1/send-email")
async def send_email(email: EmailSchema):
	q.enqueue(send_email_task, email)
	return JSONResponse(status_code=200, content={"message": "email has been sent"})

@notify.post('/v1/send-email/backgroundtasks')
def send_email_backgroundtasks(email: EmailSchema,background_tasks: BackgroundTasks):
	q.enqueue(send_email_background_task, background_tasks, email)
	# send_email_background_task(background_tasks, email)
	return JSONResponse(status_code=200, content={"message": "email has been sent"})
