from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def contactId_validator(self) -> 'AlienContact':
        if self.contact_id[0:2] != 'AC':
            raise ValueError('contact id must start with AC')
        if (self.contact_type.value.lower() == 'physical'
                and self.is_verified is False):
            raise ValueError("Physical contacts must be verified")
        if (self.contact_type.value.lower() == 'telepathic'
                and self.witness_count < 3):
            raise ValueError("telepathic contact require at least 3 witnesses")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError("Strong signals requirie received message")

        return self


# def old():
#     contacts: list[AlienContact] = []
#     failed: list[str] = []
#     for contact in ALIEN_CONTACTS:
#         try:
#             balbla = AlienContact(
#                 contact_id=contact.get('contact_id'),
#                 timestamp=contact.get('timestamp'),
#                 location=contact.get('location'),
#                 contact_type=contact.get('contact_type'),
#                 signal_strength=contact.get('signal_strength'),
#                 duration_minutes=contact.get('duration_minutes'),
#                 witness_count=contact.get('witness_count'),
#                 message_received=contact.get('message_received'),
#             )
#             contacts.append(balbla)
#         except Exception as e:
#             failed.append(contact.get('contact_id'))
#     print(contacts)
#     print()
#     print(failed)


def main():
    try:
        contact = AlienContact(
            contact_id='AC_2024_001',
            timestamp='2025-01-01 01:20:10',
            location='Area 51, Nevada',
            contact_type='radio',
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received='Greetings from Zeta Reticuli',
        )
        print("Alien Contact Log Validation")
        print("======================================")
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
        print()
        print("======================================")
    except Exception as e:
        print(e)
    try:
        contact = AlienContact(
            contact_id='AC_2024_001',
            timestamp='2025-01-01 01:20:10',
            location='Area 51, Nevada',
            contact_type='telepathic',
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli',
        )
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
