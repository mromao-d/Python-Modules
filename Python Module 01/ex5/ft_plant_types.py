class Plant:
    def __init__(self, type: str, height: float, age: int):
        self._type = type
        self._height = height
        self._age = age

    def show(self):
        print(f"{self._type}: {self.get_height():.1f}cm, {self.get_age()} days old")

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
            print(f"Height update rejected")
            return

    def set_age(self, age: int):
        if age > 0:
            self._age = age
            print(f"Age updated: {age} days")
            return
        else:
            print(f"{self._type}: Error, age can't be negative")
            print(f"Age update rejected")
            return

    def grow(self, grow_size: float):
        self._height += grow_size   

    def get_older(self, older_time: int):
        self._age += older_time


class Flower(Plant):
    def __init__(self, type: str, height: float, age: int, color: str) -> None:
        print("=== Flower")
        super().__init__(type, height, age)
        self.color = color
        self.bloomed = False
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.bloomed:
            print(" Rose has not bloomed yet")
        else:
            print(" Rose is blooming beautifully!")

    def bloom(self) -> None:
        self.bloomed = True
        print("[asking the rose to bloom]")
        self.show()


class Tree(Plant):
    def __init__(self, type: str, height: float, age: int, diameter: float) -> None:
        print("=== Tree")
        super().__init__(type, height, age)
        self.diameter = diameter
        self.show()

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.diameter: .1f}cm")

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self.get_height():.1f}cm long and {self.diameter:.1f}cm wide.")




if __name__ == '__main__':
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15, 10, 'red')
    rose.bloom()
    print()
    oak = Tree("Oak", 200, 365, 5)
    oak.produce_shade()
