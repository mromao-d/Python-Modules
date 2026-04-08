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

    def show(self):
        print(f"{self._type}: {self.get_height():.1f}cm,\
{self.get_age()} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_type(self) -> str:
        return self._type

    def set_height(self, height: float):
        if height > 0:
            self._height = height
            print(f"Height updated: {height}cm")
            return
        else:
            print(f"{self._type}: Error, height can't be negative")
            print("Height update rejected")
            return

    def set_age(self, age: int):
        if age > 0:
            self._age = age
            print(f"Age updated: {age} days")
            return
        else:
            print(f"{self._type}: Error, age can't be negative")
            print("Age update rejected")
            return

    def grow(self, grow_size: float):
        if grow_size > 0:
            self._height += grow_size

    def get_older(self, older_time: int):
        if older_time > 0:
            self._age += older_time

    def action(self, days: int = 0) -> None:
        pass


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
        print(f"[asking the {self._type} to bloom]")
        self.show()

    def print_type(self):
        print("=== Flower")

    def action(self, days: int = 0):
        self.bloom()


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

    def produce_shade(self):
        print(f"[asking the {self._type} to produce shade]")
        print(f"Tree {self._type} now produces a shade of \
{self._height:.1f}cm long and {self._diameter:.1f}cm wide.")

    def print_type(self):
        print("=== Tree")

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

    def veg_grow(self, days: int):
        print(f"[make {self.get_type()} grow and age for {days} days]")
        self.grow((days * 2) + int(days / 10))
        self.get_older(days)
        self.set_nv(days)
        self.show()

    def print_type(self):
        print("=== Vegetable")

    def action(self, days: int = 20):
        self.veg_grow(days)


if __name__ == '__main__':
    print("=== Garden Plant Types ===")
    plants: list[Plant] = [
        Flower("Rose", 15, 10, 'red'),
        Tree("Oak", 200, 365, 5),
        Vegetable("Tomato", 5, 10, "April", 0)
    ]

    for plant in plants:
        plant.show()
        plant.action()
        print()
