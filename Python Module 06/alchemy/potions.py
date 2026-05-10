from elements import create_earth, create_air
from . import elements as alchemy_elements

def healing_potion() -> str:
    return "Healing potion brewed with ’[created earth element]’ and ’[created air element]’"

def strength_potion() -> str:
    return "Strength potion brewed with ’[created fire element]’ and ’[created water element]"

# print(create_fire())
# print(create_water())
print(create_earth())
print(create_air())
