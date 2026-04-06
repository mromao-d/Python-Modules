class Plant:
    def __init__(self, type: str, height: float, age: int):
        self.type = type
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.type} {self.height:.1f}cm, {self.age} days old")

    def grow(self, grow_size: float):
        self.height += grow_size

    def get_older(self, older_time: int):
        self.age += older_time

    def show_evolution(self, grow_size: float, older_time: int):
        for i in range(self.start, self.end):
            print(f"=== Day {i} ===")
            self.show()
            self.height += grow_size
            self.age += older_time
        print(f"Growth this week: {(self.end - self.start) * grow_size:.0f}cm")


if __name__ == '__main__':
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
