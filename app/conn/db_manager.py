
from sqlalchemy.orm import Session
from .user_devices import UserDevice
from app.model.push import UserDevice as UserDeviceSchema


async def save(db: Session, user: UserDeviceSchema):
    # stmt = __upsert(tbl, values)
    db_user = UserDevice(user_id=user.user_id, token=user.token,device_info=user.device_info)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_tokens(db: Session, user_id):
    return db.query(UserDevice).filter(UserDevice.user_id == user_id)


