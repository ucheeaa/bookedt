from fastapi import APIRouter
from app.models import WaitlistEntry

router = APIRouter(prefix="/waitlist")

waitlist = []

@router.post("/")
def add_to_waitlist(entry: WaitlistEntry):
    waitlist.append(entry)
    return {"message": "Added to waitlist", "data":entry}