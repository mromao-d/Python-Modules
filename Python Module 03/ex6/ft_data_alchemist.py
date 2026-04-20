import random

def data_alchemist():
    players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']

    players_capt: list[str] = [player.capitalize() for player in players]
    players_filter: list[str] = [player for player in players if player == player.capitalize()]

    score_dict: dict[str, int] = {player: random.randint(1, 1000) for player in players_capt}
    average = sum(score_dict.values()) / len(score_dict)

    high_score: dict[str, int] = {player: score for player, score in score_dict.items() if score > average}

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {players_capt}")
    print(f"New list of capitalized names only: {players_filter}\n")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {high_score}")


if __name__ == '__main__':
    print("=== Game Data Alchemist ===\n")
    data_alchemist()
