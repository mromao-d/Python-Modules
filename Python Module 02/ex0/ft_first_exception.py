def ft_first_exception(temp_str: str) -> int:
    return int(temp_str)


def test_temperature():
    temp_str = ["25", "abc"]
    print("=== Garden Temperature ===\n")
    for el in temp_str:
        print(f"Input data is '{el}'")
        try:
            temp = ft_first_exception(el)
            print(f"Temperature is now {temp}°C\n")
        except Exception:
            raise Exception(f"Caught input_temperature error: \
invalid literal for int() with base 10: '{el}'\n")

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
