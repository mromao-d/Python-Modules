from collections.abc import Callable

# Memory Depths Test Data
initial_powers = [37, 59, 71]
power_additions = [14, 11, 18, 8, 13]
enchantment_types = ['Windy', 'Shocking', 'Flaming']
items_to_enchant = ['Cloak', 'Armor', 'Wand', 'Staff']


def mage_counter() -> Callable:
    mages = 0
    def mage_count():
        nonlocal mages
        mages += 1
        return mages

    return mage_count

def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power
    def acum(add_power: int):
        nonlocal power
        power += add_power
        return power
    return acum


def enchantment_factory(enchantment_type: str) -> Callable:
    pass

# def memory_vault() -> dict[str, Callable]:
#     pass


def main():
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"count of counter_a is {counter_a()}")
    print(f"count of counter_a is {counter_a()}")
    print(f"count of counter_b is {counter_b()}")

    print()
    acum = spell_accumulator(10)
    print(f"sum of spell_accumulator is {acum(8)}")
    print(f"sum of spell_accumulator is {acum(3)}")
    print(f"sum of spell_accumulator is {acum(4)}")


if __name__ == '__main__':
    main()
