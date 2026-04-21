import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router
from core.settings import settings

app = FastAPI()
app.include_router(router)
app.add_middleware(CORSMiddleware, allow_origins=settings.app.cors_allow)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.reload,
        workers=settings.app.workers,
    )
