from fastapi import FastAPI
from routers import ki
from routers import time

app = FastAPI()

app.include_router(ki.router)
app.include_router(time.router)