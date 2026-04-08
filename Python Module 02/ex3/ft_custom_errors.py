class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def test_errors():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught {type(e).__name__}: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught {type(e).__name__}: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == '__main__':
    test_errors()
