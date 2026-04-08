def ft_water_reminder():
    days = input("Days since last watering: ")

    if (int(days) > 2):
        return print("Water the plants!")
    print("Plants are fine")
