import alchemy.grimoire.dark_validator


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    txt = (
        f"{spell_name}: "
        f"{alchemy.grimoire.dark_validator.validate_ingredients(ingredients)}"
    )
    return txt
