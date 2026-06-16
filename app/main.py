from fastapi import FastAPI

from app.core.config import settings
from app.database import Base, engine
from app.models import User
from app.routes import user_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(user_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME
    }