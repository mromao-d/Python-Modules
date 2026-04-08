def show_stats(Plant, **kargs):
    print(f"[statistics for {Plant.get_type()}]")
    Plant._stats.display(**kargs)


class Plant:
    def __init__(
        self,
        type: str,
        height: float,
        age: int
    ) -> None:
        self._type = type
        self._height = height
        self._age = age
        self._stats = self._Stats()

    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._show_shade = 0

        def _inc_grow(self) -> None:
            self._grow_calls += 1

        def _inc_age(self) -> None:
            self._age_calls += 1

        def _inc_show(self) -> None:
            self._show_calls += 1

        def _inc_shade(self) -> None:
            self._show_shade += 1

        def display(self, **kargs) -> None:
            is_tree = kargs.get("is_tree")
            if is_tree is None:
                print(f"Stats: {self._grow_calls} grow, {self._age_calls} \
age, {self._show_calls} show")
            else:
                print(f"Stats: {self._grow_calls} grow, \
{self._age_calls} age, {self._show_calls} show")
                print(f" {self._show_shade} shade")

    def show(self) -> None:
        print(f"{self._type}: {self.get_height():.1f}cm, \
{self.get_age()} days old")
        self._stats._inc_show()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_type(self) -> str:
        return self._type

    def set_height(self, height: float) -> None:
        if height > 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._type}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age > 0:
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._type}: Error, age can't be negative")
            print("Age update rejected")

    def grow(self, grow_size: float) -> None:
        if grow_size > 0:
            self._height += grow_size
            self._stats._inc_grow()

    def get_older(self, older_time: int) -> None:
        if older_time > 0:
            self._age += older_time
            self._stats._inc_age()

    def print_type(self):
        print(f"=== {self.__class__.__name__}")

    def action(self, days: int = 0) -> None:
        pass

    @staticmethod
    def age_checker(age: int):
        print(f"Is {age} days more than a year? -> {age > 365}")

    @classmethod
    def anonymous_plant(cls):
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    def __init__(
        self,
        type: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(type, height, age)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._bloomed:
            print(f" {self._type} has not bloomed yet")
        else:
            print(f" {self._type} is blooming beautifully!")

    def bloom(self) -> None:
        self._bloomed = True
        self.grow(8)
        print(f"[asking the {self._type} to bloom]")
        self.show()

    def action(self, days: int = 0):
        self.bloom()


class Seed(Flower):
    def __init__(self, type, height, age, color) -> None:
        super().__init__(type, height, age, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def add_seeds(self, nb: int) -> None:
        self._seeds += nb

    def bloom(self) -> None:
        print(f"[make {self._type} grow, age and bloom]")
        self._bloomed = True
        self.grow(30)
        self.get_older(20)
        self.add_seeds(42)
        self.show()
        show_stats(self)


class Tree(Plant):
    def __init__(
        self,
        type: str,
        height: float,
        age: int,
        diameter: float
    ) -> None:
        super().__init__(type, height, age)
        self._diameter = diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._diameter:.1f}cm")
        show_stats(self, is_tree=True)

    def produce_shade(self):
        print(f"[asking the {self._type} to produce shade]")
        print(f"Tree {self._type} now produces a shade \
of {self._height:.1f}cm long and {self._diameter:.1f}cm wide.")
        self._stats._inc_shade()
        show_stats(self, is_tree=True)

    def action(self, days: int = 0):
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
        self,
        type: str,
        height: float,
        age: int,
        hs: str,
        nv: float
    ) -> None:
        super().__init__(type, height, age)
        self._hs = hs
        self._nv = nv

    def set_nv(
        self,
        val: float
    ) -> None:
        self._nv += val

    def show(self):
        super().show()
        print(f" Harvest season: {self._hs}")
        print(f" Nutritional value: {self._nv}")
        show_stats(self)

    def veg_grow(self, days: int):
        print(f"[make {self.get_type()} grow and age for {days} days]")
        self.grow((days * 2) + int(days / 10))
        self.get_older(days)
        self.set_nv(days)
        self.show()

    def action(self, days: int = 20):
        self.veg_grow(days)


if __name__ == '__main__':
    plants: list[Plant] = [
        Flower("Rose", 15, 10, 'red'),
        Tree("Oak", 200, 365, 5),
        Seed("Sunflower", 80, 45, "yellow")
    ]
    anonymous = Plant.anonymous_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    plants[0].age_checker(30)
    plants[0].age_checker(400)

    for plant in plants:
        print()
        plant.print_type()
        plant.show()
        plant.action()

    print()
    anonymous.show()
    show_stats(anonymous)
