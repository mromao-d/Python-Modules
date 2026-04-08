def ft_split(argv: str) -> list[str]:
    out: list = []
    i = 0
    while i < len(argv):
        el: str = ""
        while i < len(argv) and argv[i] != "," and argv[i] != " ":
            el += argv[i]
            i += 1
        if el != "":
            out += [el]
        while i < len(argv) and (argv[i] == "," or argv[i] == " "):
            i += 1
    return out


def get_player_pos():
    try:
        cords = input("Enter new coordinates as floats in format 'x,y,z': ")
        for cord in cords:
            print(cord)
    except Exception as e:
        raise Exception("Shit happened")


if __name__ == '__main__':
    el = ft_split("1 , 2 , 3")
    print(el[0:2])
    # try:
    #     get_player_pos()
    # except Exception as e:
    #     print(e)

