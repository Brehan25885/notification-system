import uvicorn
from fastapi import FastAPI
from app.router.email import notify
from app.router.sms import sms
from app.router.push import pushnotify
from app.config import get_settings
import logging

app = FastAPI(title='Notifications')

@app.get('/')
def index():
	return 'Hello World'
app.include_router(notify, prefix="/email", tags=['notify'])
app.include_router(sms, prefix="/sms", tags=['sms'])
app.include_router(pushnotify, prefix="/push", tags=['push'])
# if __name__ == '__main__':
# 	uvicorn.run('main:app', reload=True,host=get_settings().db_host, port=get_settings().port)

