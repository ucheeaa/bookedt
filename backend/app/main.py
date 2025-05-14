from fastapi import FastAPI
from app.routes import waitlist
from app.routes import appointments

app = FastAPI()

app.include_router(appointments.router)
app.include_router(waitlist.router)