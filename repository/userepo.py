from schemas import userschema
from models import usermodel 
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import uuid
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(request: userschema.UserCreate, db: Session):
    id = str(uuid.uuid4())
    hashedpass = pwd_context.hash(request.password)
    new_user = usermodel.User(name=request.name, username=request.username, email=request.email, id=id, password = hashedpass)
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        msg = str(e.orig).split(".")
        #"This %s is already exist".format(msg[1])
        msgstr = "This "+msg[1]+ " already exist"
        raise ValueError(msgstr)

    db.refresh(new_user)
    return new_user
    




