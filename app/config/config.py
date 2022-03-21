from pathlib import Path
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
	app_name = "Notify"
	app_version = "1.0.0"
	port = 8080
	messaging_credential_path = "/var/credential/key.json"
	db_host = "127.0.0.1"
	db_user = "root"
	db_pass = "12345678"
	db_schema = "pi-notify"
	max_idle_conn = 1
	max_open_conn = 2
	max_conn_lifetime = 30
	debug = True
	MAIL_USERNAME = "example@example.com"
	MAIL_PASSWORD="pass"
	MAIL_FROM="example@example.com"
	MAIL_PORT=587
	MAIL_SERVER="smtp.gmail.com"
	MAIL_FROM_NAME="test"
	MAIL_TLS=True,
	MAIL_SSL=False,
	USE_CREDENTIALS=True,
	TEMPLATE_FOLDER=Path(__file__).parent.parent / 'templates/email'
	TWILIO_ACCOUNT_SID = "##"
	TWILIO_AUTH_TOKEN = "kdk"
	TWILIO_PHONE_NUMBER="TWILIO_PHONE_NUMBER"
	FIREBASE_API_KEY = "FIREBASE"
	db_schema_test="test"


	class Config:
		ENV_FILE = ".env"
		env_file = Path(__file__).parents[2] / ENV_FILE


@lru_cache()
def get_settings():
	return Settings()
