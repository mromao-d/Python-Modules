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
            f"{self.name} is a {self.type} type Creature"
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
        self.transformed = 0

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
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str = None) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(
    Creature,
    HealCapability
):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str = None) -> str:
        return "Bloomelle heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class Shiftling(
    Creature,
    TransformCapability
):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformed:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"
    
    def transform(self, target: str = None) -> str:
        if target == None:
            target = "sharper"
        self.transformed = 1
        return f"{self.name} shifts into {target} form!"
    
    def revert(self, target: str = None) -> str:
        if target == None:
            target = "normal"
        self.transformed = 0
        return f"{self.name} returns to {target}."


class Morphagon(
    Creature,
    TransformCapability
):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformed:
            return "Morphagon attacks normally."
        return "Morphagon unleashes a devastating morph strike!"

    def transform(self, target: str = None) -> str:
        if target == None:
            target = "dragonic"
        self.transformed = 1
        return f"{self.name} morphs into {target} battle form!"
    
    def revert(self, target: str = None) -> str:
        if target == None:
            target = "normal"
        self.transformed = 0
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class IsValidError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class NormalStrategy(BattleStrategy):
    '''
    suitable for any Creature, that will simply use the
    attack method during the tournament.
    '''
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise IsValidError(f"{creature.name} is not a Creature")
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    '''
    suitable for Creature with transform capabilities,
    that will transform, attack, and revert during the tournament.
    '''
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise IsValidError(f"Battle Error, aborting tournment: Invalide Creature '{creature.name}' for this aggressive strategy")
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):
    '''
    suitable for Creature with healing capabilities, that
    will attack and then heal during the tournament.
    '''
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise IsValidError(f"Battle Error, aborting tournment: Invalide Creature '{creature.name}' for this defensive strategy")
        return [creature.attack(), creature.heal()]
        # return [creature.attack()]
