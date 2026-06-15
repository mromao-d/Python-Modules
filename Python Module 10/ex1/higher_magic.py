from collections.abc import Callable


test_values = [21, 23, 8]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def hit(target: str, power: int)-> str:
    return f"target {target} is hit with {power} power"


def hit_back(target: str, power: int)-> str:
    return f"target {target} hits back with {power} power"


def hit_aa(target: str, power: int)-> str:
    return f"aa target {target} hits back with {power} power"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, multiplier * power)


def condition(target: str, power: int)-> str:
    if target == 'asap' and power > 0:
        return True
    return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def print_fizz() -> str:
        return "Spell fizzled"

    return lambda target, power: spell(target, power) if condition(target, power) else print_fizz()


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: sorted([spell(target, power) for spell in spells])


def main():
    try:
        target = 'chocolate mouse'
        power = 10
        print(hit(target, power))
        print(hit_back(target, power))
        print()

        print("spell_combiner")
        comb = spell_combiner(hit, hit_back)
        print(comb(target, power))
        print()

        print("power_amplifier")
        amp = power_amplifier(hit, 3)
        print(amp(target, power))
        print()

        print("conditional_caster")
        cond = conditional_caster(condition, hit)
        print(f"{cond(target, power)}")
        print(f"{cond('asap', 10)}")
        print()

        print("spell_sequence")
        sort = spell_sequence([hit, hit_back, hit_aa])
        print(f"{sort(target, power)}")

    except Exception as e:
        raise type(e)(f"{type(e).__name__} || {e}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
