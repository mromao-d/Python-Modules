def ft_count_harvest_iterative() -> None:
    days = input("Days until harvest: ")

    for i in range(1, int(days) + 1):
        print(f"Day {i}")
    print("Harvest time!")
