def lead_to_gold() -> str:
    from ..elements import create_air
    from alchemy.potions import strength_potion
    from elements import create_fire
    txt = (
        "Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' and '{strength_potion()}'"
        f" mixed with '{create_fire()}'"
    )
    return txt
