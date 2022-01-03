# Driver Of Api

from fastapi import FastAPI
from routers import auth
from models import usermodel 
from database import engine

app = FastAPI()


# Database Models
usermodel.Base.metadata.create_all(bind=engine)

# all routers
app.include_router(auth.router)


@app.get("/ping")
async def root():
    return {"message": "Pong!!"}