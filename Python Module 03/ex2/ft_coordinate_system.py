import math

class SyntaxError(Exception):
    def __init__(self, message='Invalid syntax'):
        super().__init__(message)


def cords_flt(input: str) -> tuple[float, float, float]:
    cords = input.split(',')
    if len(cords) != 3:
        raise SyntaxError
    result = []
    for cord in cords:
        try:
            result.append(float(cord.strip()))
        except (Exception) as e:
            raise type(e)(f"Error on parameter '{cord.strip()}': {e}")
    return tuple(result)


def get_player_pos() -> tuple[float, float, float]:
    try:
        cords = input("Enter new coordinates as floats in format 'x,y,z': ")
        x, y, z = cords_flt(cords)
        print(f"Got a first tuple: {x, y, z}")
        print(f"It includes: X={x}, Y={y}, Z={z}")
        print(f"Distance to center: {math.sqrt(x ** 2 + y ** 2 + z ** 2): .4f}")
        return x, y, z

    except Exception as e:
        print(e)
        return get_player_pos()


def get_cords_two(x: float, y: float, z: float):
    try:
        cords = input("Enter new coordinates as floats in format 'x,y,z': ")
        x, y, z = cords_flt(cords)
        print(f"Distance to center: {math.sqrt((x- x_one) ** 2 + (y - y_one) ** 2 + (z - z_one) ** 2): .4f}")

    except Exception as e:
        print(e)
        get_player_pos()


if __name__ == '__main__':
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    x_one, y_one, z_one = get_player_pos()
    print("\nGet a second set of coordinates")
    get_cords_two(x_one, y_one, z_one)
