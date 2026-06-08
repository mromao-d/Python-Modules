from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str=Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str=Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float=Field(ge=0, le=10)
    duration_minutes: int=Field(ge=1, le=1440)
    witness_count: int=Field(ge=1, le=100)
    message_received: Optional[str]=Field(max_length=500)
    is_verified: bool=Field(default=False)

    @field_validator('contact_id')
    def contactId_validator(cls, value):
        if value[0:2] != 'AC':
            raise ValueError('contact id must start with AC')
        return value



def main():
    contact = AlienContact(
        contact_id = 'AC_2024_001',
        timestamp = '2025-01-01 01:20:10',
        location = 'Area 51, Nevada',
        contact_type = 'radio',
        signal_strength = 8.5,
        duration_minutes = 45,
        witness_count = 5,
        message_received = 'Greetings from Zeta Reticuli',
    )
    print(f"Alien Contact Log Validation")
    print(f"======================================")
    print(f"Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")


if __name__ == '__main__':
    main()
