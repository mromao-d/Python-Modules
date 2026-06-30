from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> float:
        start_time = time.perf_counter()
        print(f"casting {func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        exec_time = end_time - start_time
        print(f"Spell completed in {exec_time:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball():
    time.sleep(1)
    return f"Result: {fireball.__name__} cast!"


def power_validator(min_power: int) -> Callable:
    def exec_power(func) -> Callable | str:
        @wraps(func)
        def wrapper(*args, **kargs):
            if args and isinstance(args[-1], int):
                power = args[-1]
            else:
                power = kargs.get("power")
            if power is None:
                raise ValueError("Power args is needed")
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kargs)

        return wrapper

    return exec_power


@power_validator(10)
def power(power: int) -> str:
    return f"Successfully cast spell_name with {power} power"


def retry_spell(max_attempts: int) -> Callable:
    def retry_exec(func) -> Callable:

        @wraps(func)
        def wrapper(*args, **kargs) -> Callable | str:
            for i in range(max_attempts):
                try:
                    result = func(*args, **kargs)
                    return result
                except Exception:
                    if i + 1 == max_attempts:
                        return (
                            f"Spell cast failed after {max_attempts} attempts"
                        )
                    msg = (
                        "Spell failed, retrying..."
                        f"(attempt {i + 1}/{max_attempts})"
                    )
                    print(msg)
            return func(*args, **kargs)

        return wrapper

    return retry_exec


@retry_spell(3)
def test_retry():
    # return f"a is {a}"
    return "a is {a}"


@retry_spell(3)
def test_retry_2():
    return "Waaaaaaagh spelled !"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    try:
        print("Testing spell timer...")
        print(fireball())
        print()

        print("Testing power_validator...")
        print(power(power=9))
        print(power(power=11))
        print(power(11))
        print()

        print("Testing test_retry...")
        print(test_retry())
        print(test_retry_2())
        print()

        print("Testing MageGuild...")
        mage = MageGuild()
        print(mage.validate_mage_name("aas"))
        print(mage.validate_mage_name("aa2s"))
        print(mage.cast_spell("asdasds", 15))
        print(mage.cast_spell("asdasds", power=5))
    except Exception as e:
        raise type(e)(f"{type(e).__name__} || {e}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
