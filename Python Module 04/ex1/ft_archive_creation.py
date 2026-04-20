import sys

class UsageError(Exception):
    pass


def transform_data(args: list[str]):
    file: str = args[0]
    try:
        new_doc: str = ""
        with open(file, 'r') as fd:
            print("Transform data:\n---\n")
            line = fd.readline().rstrip()
            while line:
                new_doc += f"{line}#\n"
                print(f"{line}#")
                line = fd.readline().rstrip()

        new_file = input("\n---\nEnter new file name (or empty): ")
        if not new_file:
            print("Not saving data.")
            return None
        with open(new_file, 'w') as fd:
            print(f"saving data to '{new_file}'")
            fd.write(new_doc)   
        print(f"Data saved in file '{new_file}'\n")
    except Exception as e:
        raise type(e)(f"{e}\n")


def archive_creation(args: list[str]):
    if len(args) != 1:
        raise UsageError("Usage: ft_ancient_text.py <file>")
    file: str = args[0]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file {file}")
    try:
        with open(file, 'r') as fd:
            content = fd.read()
            print("---\n\n")
            print(content)
            print("\n---")
        print(f"File '{file}' closed.\n")
        transform_data(sys.argv[1:])
    except Exception as e:
        raise type(e)(f"Error opening file '{file}': {e}\n")
    return None


if __name__ == '__main__':
    try:
        archive_creation(sys.argv[1:])
    except Exception as e:
        print(e)
