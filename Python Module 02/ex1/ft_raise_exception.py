def ft_first_exception(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
    except Exception as e:
        raise ValueError(f"Caught input_temperature error: invalid literal for int() with base 10: '{temp_str}'\n")
    if not 0 <= temp <= 40:
        condition = "hot" if temp > 40 else "cold"
        min_max = "max 40" if temp > 40 else "min 0"
        raise ValueError(f"Caught input_temperature error: {temp_str}°C is too {condition} for plants ({min_max}°C)\n")
    print(f"Temperature is now {temp}°C\n")
    return temp


def test_temperature():
    temp_str = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature ===\n")
    for el in temp_str:
        try:
            ft_first_exception(el)
        except ValueError as e:
            print(e)

    print("All tests completed - program didn't crash!")

if __name__ == '__main__':
    test_temperature()
