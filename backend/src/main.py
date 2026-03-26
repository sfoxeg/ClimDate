import uvicorn
from fastapi import FastAPI
from core.settings import settings
from api import router

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.app.host, port=settings.app.port, reload=settings.app.reload)
