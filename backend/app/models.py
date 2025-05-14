from pydantic import BaseModel

class WaitlistEntry(BaseModel):
    id: int
    name: str
    contact_method: str  #e.g., "sms" or "email"
    contact_value: str   #phone number or email