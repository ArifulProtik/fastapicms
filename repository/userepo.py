from schemas import userschema
from models import usermodel 
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import uuid
from utils import hash





def create_user(request: userschema.UserCreate, db: Session):
    id = str(uuid.uuid4())
    new_user = usermodel.User(name=request.name, username=request.username, email=request.email, id=id, password = hash.hash.encrypt(request.password))
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
    
def get_user_byemail(key, db: Session) -> usermodel.User:
    user = db.query(usermodel.User).filter(usermodel.User.email == key).first()
    if not user:
        msg = "No User Found By "+key
        raise ValueError(msg)
    return user
    




