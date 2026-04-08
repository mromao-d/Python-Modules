import sys

if __name__ == '__main__':
    print("=== Command Quest ===")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
    i = 0
    for arg in sys.argv:
        if i == 0:
            print(f"Program name: {sys.argv[i]}")
        else:
            print(f"Argument {i}: {arg}")
        i += 1
    if i == 1:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")
