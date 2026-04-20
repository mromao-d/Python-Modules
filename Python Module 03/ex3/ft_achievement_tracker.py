import random

def gen_player_achievements():
    achievements: set[str] = {'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'}
    players = {"Alice": set(), "Bob": set(), "Charlie": set(), "Dylan": set()}
    common = set()

    for i in range(0, 10):
        for ach in players.values():
            ach.add(random.choice(list(achievements)))

    for player, ach in players.items():
        print(f"Player {player}: {ach}")

    common = set.intersection(*players.values())
    print(f"\nAll distinct achievements: {achievements}")
    print(f"\nCommon achievements: {common}\n")

    for key, value in players.items():
        others = set.union(*(v for k, v in players.items() if k != key))
        unique = value - others
        print(f"Only {key} has: {unique}")

    print()
    for key, value in players.items():
        print(f"{key} is missing: {achievements - value}")
    return


if __name__ == '__main__':
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
