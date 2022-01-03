from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from database import get_db

from schemas import userschema
from repository import userepo



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
async def signinuser(request: userschema.Userlogin):
    return
