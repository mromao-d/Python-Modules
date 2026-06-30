from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200)


def main():
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    ship = SpaceStation(
        station_id='ISS001',
        name='International Space Station',
        crew_size='6',
        power_level='85.5',
        oxygen_level='92.3',
        last_maintenance='2026-01-01 23:30:17',
        notes=None,
    )
    print(f"ID: {ship.station_id}")
    print(f"Name: {ship.name}")
    print(f"Crew: {ship.crew_size} people")
    print(f"Power: {ship.power_level}%")
    print(f"Oxygen: {ship.oxygen_level}%")
    op_txt = (
        f"Status: {None if ship.is_operational is True else 'not'} Operational"
    )
    print(op_txt)
    print("========================================")
    print("Expected validation error:")
    try:
        ship = SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size='26',
            power_level='85.5',
            oxygen_level='92.3',
            last_maintenance='2026-01-01 23:30:17',
            notes=None,
        )
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
