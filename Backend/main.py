from fastapi import FastAPI
from routes.user import router as user_router
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from sqlalchemy.sql import text
from config.database import engine
from models.user import Base  

app = FastAPI()

app.include_router(user_router, prefix="/api", tags=["User Management"])



# Create tables in the database
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application"}




@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {"status": "Database connection is working!"}
    except Exception as e:
        return {"error": str(e)}