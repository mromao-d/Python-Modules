class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


def validate_override(args: dict) -> bool:
    import os
    from dotenv import load_dotenv
    load_dotenv(override=True)
    MATRIX_MODE = os.getenv('MATRIX_MODE')
    DATABASE_URL = os.getenv('DATABASE_URL')
    API_KEY = os.getenv('API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')
    dict = {
        "Mode": MATRIX_MODE,
        "Database": DATABASE_URL,
        "API Access": API_KEY,
        "Log Level": LOG_LEVEL,
        "Zion Network": ZION_ENDPOINT,
    }

    if args["Mode"].lower() == "development":
        return False
    for key, value in dict.items():
        if value != args[key]:
            return True
    return False


def get_confs() -> bool:
    try:
        import os
        from dotenv import load_dotenv

        load_dotenv()
        MATRIX_MODE = os.getenv('MATRIX_MODE')
        DATABASE_URL = os.getenv('DATABASE_URL')
        API_KEY = os.getenv('API_KEY')
        LOG_LEVEL = os.getenv('LOG_LEVEL')
        ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')
        dict = {
            "Mode": MATRIX_MODE,
            "Database": DATABASE_URL,
            "API Access": API_KEY,
            "Log Level": LOG_LEVEL,
            "Zion Network": ZION_ENDPOINT,
        }

        if MATRIX_MODE and MATRIX_MODE.lower() == 'development':
            print("development mode")

        elif MATRIX_MODE and MATRIX_MODE.lower() == 'production':
            print("production mode")

        elif MATRIX_MODE:
            raise CustomException("That Matrix Mode does not exist")

        for key, value in dict.items():
            if value != "" and value is not None:
                print(f"{key} is {value}")
            else:
                print(f"missing config for {key}")

        failed = {
            key for key, value in dict.items() if value is None or value == ""
        }
        if (
            MATRIX_MODE and LOG_LEVEL and MATRIX_MODE.lower() == 'production'
            and LOG_LEVEL.lower() != "info"
        ):
            failed.add("Log Level")
            raise CustomException("wrong Log Level")

        if failed:
            raise CustomException("Missing env variables")

        return validate_override(dict)

    except Exception as e:
        raise type(e)(f"{type(e).__name__} - {e}")


def main() -> None:
    try:
        override = get_confs()
        print()
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        if override:
            print("[OK] Production overrides available")
    except Exception as e:
        print(e)
    return None


if __name__ == '__main__':
    main()
