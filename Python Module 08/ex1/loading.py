# create venv -> python3 -m venv <name>
# install dependencies
# run pip3 freeze >> requirements.txt
# pip install -r requirements.txt

# poetry init
# poetry add <package>
# poetry install
# poetry run pyhton <program_name.py>


# using marketstack.com API to extract data
def read_api_data() -> dict:
    try:
        import os
        from dotenv import load_dotenv
        import requests
        load_dotenv()

        url = os.getenv('API_URL')
        api_key = os.getenv('API_KEY')

        offset = 0
        limit = 100
        all_data = []
        while True:
            params = {
                "access_key": api_key,
                "symbols": "AAPL",
                "sort": "DESC",
                "date_from": "2025-01-01",
                "date_to": "2026-06-01",
                "offset": offset,
                "limit":limit,
            }

            response = requests.get(f"{url}eod", params=params)
            if response.status_code != 200:
                raise requests.RequestException(f"Invalid response: {response.status_code}")
            
            payload = response.json()
            page_data = payload.get('data', [])
            pagination = payload.get('pagination', {})

            if not page_data:
                break

            all_data.extend(page_data)

            # prepare next request
            count = pagination.get('count', len(page_data))
            total = pagination.get('total')
            offset += count

            if count < limit:
                break

        return {
            "pagination": {
                "total": len(all_data)
            },
            "data": all_data
        }


    except Exception as e:
        raise type(e)(f"Error is {e}")


def check_libs() -> bool:
    '''
    Validates if all libs exist
    Returns True if all exist
    '''
    ok = {}
    nok = []

    imports = list(set(["pandas","numpy", "requests","matplotlib"]))

    for module in imports:
        try:
            mod = __import__(module)
            ok[mod.__name__]= mod.__version__
        except Exception as e:
            nok.append(module)
            txt = (
                f"Error is {e}. "
                f"Please install it with pip (pip install {module}) "
                f" or with poetry (poetry add {module})"
            )
            print(txt)

    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    libs = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": " Network access ready",
        "matplotlib": " Visualization ready",
    }
    for lib, version in ok.items():
        print(f"[OK] {lib} ({lib}) - {libs[lib]}")
    for lib in nok:
        print(f"[NOK] {lib} is not installed")
    if len(nok) == 0:
        return True
    return False


def read_data() -> list:
    import pandas as pd
    import numpy as np

    data = {'date':[], 'value':[]}
    dates = pd.date_range("2025-01-01", "2025-02-01")
    data["date"].extend(dates)
    data["value"].extend(np.random.randint(0, 1000, len(dates)))

    return data


def main() -> None:
    try:
        if check_libs() == False:
            return None
        import pandas as pd
        import matplotlib.pyplot as plt

        print()
        print("Analyzing Matrix data...")
        data = read_data()
        pd_df = pd.DataFrame(data, columns=['date', 'value'])
        print(f"Processing {len(pd_df)} data points...")
        pd_df['date'] = pd.to_datetime(pd_df['date'])

        plt.plot(pd_df['date'], pd_df['value'], linestyle = 'solid')

        # Add title and axis labels
        plt.title('Time Series Plot')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig('matrix_analysis.png')

        print("Generating visualization...")
        print()
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
