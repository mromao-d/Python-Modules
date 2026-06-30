from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime


class Ranks(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Ranks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=2, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        if self.mission_id[0] != 'M':
            raise ValueError('Mission id must start with "M"')
        dudes = [
            dude for dude in self.crew
            if dude.rank.value.lower() in ['commander', 'captain']
        ]
        if not len(dudes):
            raise ValueError('Min of 1 cap or commander')
        dudes = [dude for dude in self.crew if dude.years_experience >= 5]
        if self.duration_days > 365 and (len(dudes) / len(self.crew) < 0.5):
            raise ValueError('at least 50% of crew must be experient')
        if any(dude.is_active is False for dude in self.crew):
            raise ValueError('all members must be active')
        return self


# def create_member(**kargs) -> CrewMember:
#     return CrewMember(
#             member_id=kargs.get('member_id', None),
#             name=kargs.get('name', None),
#             rank=kargs.get('rank', None),
#             age=kargs.get('age', None),
#             launch_date=kargs.get('launch_date', None),
#             specialization=kargs.get('specialization', None),
#             years_experience=kargs.get('years_experience', None),
#     )

def success():
    try:
        memb1 = CrewMember(
            member_id="aaa",
            name="Sarah Connor",
            rank="commander",
            age=35,
            launch_date='2025-01-01 01:20:10',
            specialization="mission command",
            years_experience=0,
            # is_active=False,
        )
        memb2 = CrewMember(
            member_id="aab",
            name="John Smith",
            rank="lieutenant",
            age=26,
            launch_date='2025-01-01 01:20:10',
            specialization="Navigation",
            years_experience=10,
        )

        memb3 = CrewMember(
            member_id="aac",
            name="Alice Johnson",
            rank="officer",
            age=65,
            launch_date='2025-01-01 01:20:10',
            specialization="Engineering",
            years_experience=5,
        )

        mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date='2025-01-01 01:20:10',
            duration_days=900,
            crew=[memb1, memb2, memb3],
            mission_status='doing',
            budget_millions='2500.0',
        )
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"destination: {mission.destination}")
        print(f"duration_days: {mission.duration_days}")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"crew size: {len(mission.crew)}")
        print("crew members:")
        for mem in mission.crew:
            print(f" - {mem.name} ({mem.rank.value}) - {mem.specialization}")
    except Exception as e:
        print(e)


def insuccess():
    try:
        memb1 = CrewMember(
            member_id="aaa",
            name="Sarah Connor",
            rank="lieutenant",
            age=35,
            launch_date='2025-01-01 01:20:10',
            specialization="mission command",
            years_experience=0,
            # is_active=False,
        )
        memb2 = CrewMember(
            member_id="aab",
            name="John Smith",
            rank="lieutenant",
            age=26,
            launch_date='2025-01-01 01:20:10',
            specialization="Navigation",
            years_experience=10,
        )
        memb3 = CrewMember(
            member_id="aac",
            name="Alice Johnson",
            rank="officer",
            age=65,
            launch_date='2025-01-01 01:20:10',
            specialization="Engineering",
            years_experience=5,
        )

        mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date='2025-01-01 01:20:10',
            duration_days=900,
            crew=[memb1, memb2, memb3],
            mission_status='doing',
            budget_millions='2500.0',
        )
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"destination: {mission.destination}")
        print(f"duration_days: {mission.duration_days}")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"crew size: {len(mission.crew)}")
        print("crew members:")
        for mem in mission.crew:
            print(f" - {mem.name} ({mem.rank.value}) - {mem.specialization}")
    except Exception as e:
        print(e)


def main():
    print('Space Mission Crew Validation')
    print('=========================================')
    print('Valid mission created:')
    success()
    print()
    print('=========================================')
    print('Expected validation error: ')
    insuccess()


if __name__ == '__main__':
    main()
