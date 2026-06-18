from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.database import Base, engine
from backend.app.models import User, Task
from backend.app.routes import user_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(user_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME
    }