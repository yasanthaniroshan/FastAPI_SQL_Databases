from fastapi import FastAPI, Depends, HTTPException
from models import Base, User
from schemas import UserSchema
from database import engine,SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def home():
    return {"message": "Hello, World!"}

@app.post("/adduser")
async def add_user(request:UserSchema, db: Session = Depends(get_db)):
    user = User(name=request.name, email=request.email, nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/{user_name}")
async def get_users(user_name,db: Session = Depends(get_db)):
    users = db.query(User).filter(User.name == user_name).first()
    return users