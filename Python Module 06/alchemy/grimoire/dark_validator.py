from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    allowed = dark_spell_allowed_ingredients()

    for el in allowed:
        if el in ingredients:
            return "VALID"
    return "INVALID"
