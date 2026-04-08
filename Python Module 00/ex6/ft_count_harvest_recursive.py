def ft_count_harvest_recursive() -> None:
    def print_shit(min: int, days: int):
        if min <= days:
            print(f"Day {min}")
            print_shit(min + 1, days)
    days = int(input("Days until harvest: "))
    print_shit(1, days)
    print("Harvest time!")
