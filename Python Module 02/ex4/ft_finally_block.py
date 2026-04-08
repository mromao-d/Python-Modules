class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Caught PlantError: Invalid\
 plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list) -> None:
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == '__main__':
    print("=== Garden Watering System ===")
    test_watering_system(['Tomato', 'Lettuce', 'Carrots'])
    test_watering_system(['Tomato', 'lettuce', 'Carrots'])

    print("\nCleanup always happens, even with errors!")
