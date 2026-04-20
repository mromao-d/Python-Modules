import sys

class UsageError(Exception):
    pass


def retrieve_shit(args: list[str]):
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
        print(f"File '{file}' closed.")
    except Exception as e:
        raise type(e)(f"Error opening file '{file}': {e}\n")
    return None


if __name__ == '__main__':
    try:
        retrieve_shit(sys.argv[1:])
    except Exception as e:
        print(e)
