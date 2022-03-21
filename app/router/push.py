from fastapi import APIRouter,Depends
from app.model.task_manager import save_push_notification_user_data,send_push_notification
from app.model.push import  UserDevice, UserDevicePayload, Response, MessagePayload
from app.conn.db import SessionLocal, engine
from app.conn import user_devices
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

user_devices.Base.metadata.create_all(bind=engine)

pushnotify = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
@pushnotify.post("/v1/register", response_model=UserDevice, status_code=201)
async def register(payload: UserDevicePayload, db: Session = Depends(get_db)):
	return await save_push_notification_user_data(db,payload)




@pushnotify.post("/v1/message", response_model=Response, status_code=201)
async def send_message(payload: MessagePayload,db: Session = Depends(get_db)):
	await send_push_notification(payload,db)
	return JSONResponse(status_code=200, content={"message": "message has been sent"})