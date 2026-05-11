from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(
        self,
        name: str,
        type: str,
    ) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        '''
        returns a standart message
        with name and type of the creature
        '''
        txt = (
            f"{self.name} is a {self.type} Creature"
        )
        return txt


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = None):
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.attack = 0

    @abstractmethod
    def transform(self, target: str = None) -> str:
        pass

    @abstractmethod
    def revert(self, target: str = None) -> str:
        pass


class Sproutling(
    Creature,
    HealCapability
):

