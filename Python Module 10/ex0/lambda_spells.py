artifacts = [
    {'name': 'Water Chalice', 'power': 70, 'type': 'armor'},
    {'name': 'Ice Wand', 'power': 92, 'type': 'weapon'},
    {'name': 'Ice Wand', 'power': 66, 'type': 'accessory'},
    {'name': 'Wind Cloak', 'power': 107, 'type': 'weapon'}
]

mages = [
    {'name': 'Jordan', 'power': 94, 'element': 'wind'},
    {'name': 'Kai', 'power': 94, 'element': 'earth'},
    {'name': 'Sage', 'power': 52, 'element': 'shadow'},
    {'name': 'Luna', 'power': 67, 'element': 'light'},
    {'name': 'Phoenix', 'power': 96, 'element': 'lightning'}
]

spells = ['meteor', 'tsunami', 'lightning', 'freeze']

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get('power'))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get('power') >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_p = filter(lambda x: x.get('power') == max(mage.get('power') for mage in mages), mages)
    min_p = filter(lambda x: x.get('power') == min(mage.get('power') for mage in mages), mages)
    total_p = sum(mage.get('power') for mage in mages)
    # out: dict[int, int, float] = {}
    out = {
        'max_power': list(max_p)[0].get('power'),
        'min_power': list(min_p)[0].get('power'),
        'avg_power': round(total_p / len(mages), 2),
    }
    return out


if __name__ == '__main__':
    print("Testing artifact sorter...")
    print("Sorted list:")
    sorted = artifact_sorter(artifacts)
    for i in range(len(sorted)):
        print(f"{i} - {sorted[i]}")
    print()
    min_strength = 90
    print(f"Mages stronger than: {min_strength}")
    filtered = power_filter(mages, min_strength)
    for i in range(len(filtered)):
        print(f"{i} - {filtered[i]}")
    print()
    print("Spells transformed:")
    print(spell_transformer(spells))
    print()
    print("Spells stats:")
    for key, value in mage_stats(mages).items():
        print(f"{key}: {value}")
