def get_player_pos():
    try:
        cords = input("Enter new coordinates as floats in format 'x,y,z': ")
        for cord in cords:
            print(cord)
    except Exception as e:
        raise Exception("Shit happened")


if __name__ == '__main__':
    try:
        get_player_pos()
    except Exception as e:
        print(e)

