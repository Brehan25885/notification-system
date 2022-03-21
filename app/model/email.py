from typing import List
from pydantic import EmailStr, BaseModel


class BodySchema(BaseModel):
	title: str
	name: str

class EmailSchema(BaseModel):
	subject:str
	email: List[EmailStr]
	body: BodySchema
