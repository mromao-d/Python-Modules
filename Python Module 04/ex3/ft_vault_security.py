def read_file(filename: str):
    try:
        with open(filename, 'r') as fd:
            content = fd.read()
            return (True, content)
    except Exception as e:
        raise type(e)(e)


def write_file(filename: str, content: str):
    try:
        with open(filename, 'w') as fd:
            fd.write(content)
            return (True, 'Content successfully written to file')
    except Exception as e:
        raise type(e)(e)


def secure_archive(filename: str, operation: str = None, content: str = None):
    try:
        if operation == 'read':
            return read_file(filename)
        if operation == 'write':
            return write_file(filename, content)
    except Exception as e:
        return False, f"{e}"
    return False, "Invalid operaion"



if __name__ == '__main__':
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", operation='read'))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ex3/ancient_fragment.txt", operation='read'))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("ex3/test.txt", operation='write', content="Fuck you"))
    print()
