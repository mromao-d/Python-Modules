def healing_potion() -> str:
    from .elements import create_air, create_earth
    txt = (
        f"Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )
    return txt


def strength_potion() -> str:
    from elements import create_fire, create_water
    txt = (
        f"Strength potion brewed with "
        f"'{create_fire()}' and '{create_water()}'"
    )
    return txt
