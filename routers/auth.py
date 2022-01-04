from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_406_NOT_ACCEPTABLE
from database import get_db

from schemas import userschema
from repository import userepo
from utils import hash
from auth import jwthandler



router = APIRouter(
    prefix="/api/v1/user",
    tags=["Authentication"]
)
#response_model=userschema.Userinfo
@router.post("/signup",response_model=userschema.Userinfo)
async def createUser(user: userschema.UserCreate, db: Session = Depends(get_db)):
    try:
        newuser = userepo.create_user(user, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.args)
    
    return newuser
@router.post("/signin")
async def signinuser(request: userschema.Userlogin, db: Session = Depends(get_db)):
    email = request.email.strip()
    try:
        user = userepo.get_user_byemail(email, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.args)
    if hash.hash.verify_password(request.password, user.password):
        access_token = jwthandler.signAcessJWT(user.id)
        refresh_token = jwthandler.signRefreshJWT(user.id)
        res = {
            "access": access_token,
            "refresh": refresh_token
        }
        return res
    raise HTTPException(status_code=HTTP_406_NOT_ACCEPTABLE, detail="Password Incorrect")
