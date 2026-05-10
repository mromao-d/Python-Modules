from .light_validator import validate_ingredients


def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    txt = (
        f"{spell_name}: "
        f"{ validate_ingredients(ingredients)}"
    )
    return txt
