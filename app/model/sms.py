from pydantic import BaseModel


class SMSSchema(BaseModel):
	phone: str
	body: str
