import logging
from typing import List


from app.config import get_settings
from pyfcm import FCMNotification


logger = logging.getLogger(__name__)


def send(title: str, body: str, tokens: List[str]):
	push_service = FCMNotification(api_key=get_settings().FIREBASE_API_KEY)
	try:
		result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=title, message_body=body)
		logger.info(f'sent message to {result} device(s)')
		return result
	except Exception as e:
		logger.exception("exception occur when sending message using firebase admin sdk")

