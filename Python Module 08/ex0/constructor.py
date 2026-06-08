import os

def detect_venv() -> tuple[bool, str]:
    import sys
    if sys.prefix == sys.base_prefix:
        return False, "This is NOT a virtual environment"
    return True, os.getenv('VIRTUAL_ENV')


def display_info(env_funct) -> None:
    is_env, txt = env_funct()
    print()
    if not is_env:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {os.getenv('_')}")
        print(f"Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python-m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {os.getenv('_')}")
        print(f"Virtual Environment: {os.getenv('VIRTUAL_ENV_PROMPT')}")
        print(f"Environment Path: {txt}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])

    # return None


if __name__ == '__main__':
    import site
    display_info(detect_venv)
    # print(site.getsitepackages())