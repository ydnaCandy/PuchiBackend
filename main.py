from fastapi import FastAPI
from routers import ki

app = FastAPI()

app.include_router(ki.router)
