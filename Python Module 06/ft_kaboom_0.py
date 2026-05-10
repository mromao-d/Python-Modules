import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
txt = (
    "Testing record light spell: Spell recorded: "
    f'{alchemy.grimoire.light_spell_record("Fantasy", "Earth, wind and fire")}'
)
print(txt)
