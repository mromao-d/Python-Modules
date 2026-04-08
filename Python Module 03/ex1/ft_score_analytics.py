import sys

def ft_process_scores(arg: str):
    try:
        arg_int = int(arg)
    except ValueError:
        raise ValueError(f"Invalid parameter: '{arg}'")
    return arg_int


def test_analytics(args: list):
    new_lst: list = []

    for arg in args:
        try:
            new_lst += [ft_process_scores(arg)]
        except ValueError as e:
            print(e)
    if len(new_lst) > 0:
        print(f"Scores processed: {new_lst}")
        print(f"Total Players: {len(new_lst)}")
        print(f"Total score: {sum(new_lst)}")
        print(f"Average score: {sum(new_lst) / len(new_lst)}")
        print(f"High score: {max(new_lst)}")
        print(f"Low score: {min(new_lst)}")
        print(f"Score range: {max(new_lst) - min(new_lst)}")


if __name__ == '__main__':
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        test_analytics(sys.argv[1:])


# $> python3 ft_score_analytics.py 1500 2300 1800 2100 1950
# === Player Score Analytics ===
# Scores processed: [1500, 2300, 1800, 2100, 1950]
# Total players: 5
# Total score: 9650
# Average score: 1930.0
# High score: 2300
# Low score: 1500
# Score range: 800
# $> python3 ft_score_analytics.py
# === Player Score Analytics ===
# No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
# $> python3 ft_score_analytics.py ab ac
# === Player Score Analytics ===
# Invalid parameter: 'ab'
# Invalid parameter: 'ac'
# No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...

