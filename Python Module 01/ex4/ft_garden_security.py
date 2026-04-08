class Plant:
    def __init__(self, type: str, height: float, age: int):
        self._type = type
        self._height = height
        self._age = age
        self.show()

    def show(self):
        print(f"Plant created: {self._type}: \
{self._height:.1f}cm, {self._age} days old")

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
        if grow_size < 0:
            return
        self._height += grow_size

    def get_older(self, older_time: int):
        if older_time < 0:
            return
        self._age += older_time


if __name__ == '__main__':
    rose = Plant("Rose", 15, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-25)
    rose.set_age(-30)
    type = rose.get_type()
    height = rose.get_height()
    age = rose.get_age()
    print(f"Current state: {type}: {height:.1f}cm, {age} days old")
