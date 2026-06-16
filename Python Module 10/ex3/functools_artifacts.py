from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    try:
        return reduce(operation, spells)
    except Exception as e:
        raise type(e)(f"{type(e).__name__} || {e}")


def test_partial (power: int, element: str, target:str) -> str:
    return f"{element } atacks {target} with {power} power"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    try:
        one = partial(base_enchantment, 10, "one")
        two = partial(base_enchantment, 20, "two")
        three = partial(base_enchantment, 30, "three")
        return {
            "one": one,
            "two": two,
            "three": three,
        }
    except Exception as e:
        raise type(e) (f"{type(e).__name__} || {e}")


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("number should be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# def spell_dispatcher() -> Callable[[Any], str]:
#     pass


def main():

    try:
        print("testing spell_reducer")
        items = [1, 5, 1, 7]
        # items = []
        print(spell_reducer(items, add))
        print(spell_reducer(items, mul))
        print(spell_reducer(items, max))
        print(spell_reducer(items, "asd"))
    except Exception as e:
        print(e)

    try:
        print()
        print("------------------------------------")
        print("testing partial_enchanter")
        enchants = partial_enchanter(test_partial)
        for key, value in enchants.items():
            print(f"for key {key}: {value("asdsad")}")
    except Exception as e:
        print(e)

    try:
        print()
        print("------------------------------------")
        print("testing memoized_fibonacci")
        # fib = memoized_fibonacci(3)
        # print(f"fib(0) is: {memoized_fibonacci(0)}")
        # print(memoized_fibonacci.cache_info())
        # print(f"fib(1) is: {memoized_fibonacci(1)}")
        # print(memoized_fibonacci.cache_info())
        # print(f"fib(10) is: {memoized_fibonacci(10)}")
        # print(memoized_fibonacci.cache_info())
        print(f"fib(15) is: {memoized_fibonacci(15)}")
        print(memoized_fibonacci.cache_info())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
