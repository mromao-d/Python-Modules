import random
from typing import Generator

def gen_event(players: list[str], events: list[str]):
    while (1):
        yield random.choice(players), random.choice(events)


def consume_event(lst_events: list[tuple[str, str]]):
    while lst_events:
        ran_event = random.choice(lst_events)
        print(f"Got event from list: {ran_event}")
        lst_events.remove(ran_event)

        yield lst_events


if __name__ == '__main__':
    players: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    events: list[str] = ['run', 'eat', 'sleep', 'move', 'climb', 'release', 'grab', 'swim']
    gen = gen_event(players, events)
    for i in range(0, 1000):
        player, event = next(gen)
        print(f"Event {i}: Player {player} did action {event}")

    lst_events: list[tuple[str, str]] = []
    for i in range(0, 10):
        player, event = next(gen)
        lst_events.append((player, event))
    print(f"Built list of 10 events: {lst_events}")

    for i in range(0, 10):
        gen_lst = consume_event(lst_events)
        new_lst = next(gen_lst)
        print(f"Remains in list: {new_lst}")
