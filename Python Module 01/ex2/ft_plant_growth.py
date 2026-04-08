class Plant:
    def __init__(self, type: str, height: float, age: int):
        self.type = type
        self.height = height
        self.age = age
        self.start = 1
        self.end = 8

    def show(self):
        print(f"{self.type}: {self.height: .1f}cm, {self.age} days old")

    def grow(self, grow_size: float):
        if grow_size < 0:
            return
        self.height += grow_size

    def get_older(self, older_time: int):
        if older_time < 0:
            return
        self.age += older_time

    def show_evolution(self, grow_size: float, older_time: int):
        for i in range(self.start, self.end):
            print(f"=== Day {i} ===")
            self.show()
            self.grow(grow_size)
            self.get_older(older_time)
        print(f"Growth this week: {(self.end - self.start) * grow_size:.0f}cm")


if __name__ == '__main__':
    rose = Plant("Rose", 25, 30)
    rose.show_evolution(0.8, 1)
