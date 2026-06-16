from fastapi import FastAPI

from app.core.config import settings
from app.database import Base, engine
from app.models import User


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME
    }
