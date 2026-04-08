def garden_operations(operation_number: int) -> None:
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            1 / 0
        elif operation_number == 2:
            with open("./aex1/ft_raise_exception.py") as fd:
                print(fd)
        elif operation_number == 3:
            1 + "3"
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        raise type(e)(f"Caught {type(e).__name__}: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(e)
    print("Operation completed successfully\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
