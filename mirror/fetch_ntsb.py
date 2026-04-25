import requests
import pandas as pd
from io import StringIO

URL = "https://www.ntsb.gov/_layouts/15/NTSB.Aviation/DownloadCSV.aspx"

def fetch_ntsb():
    print("[NTSB] Fetching CSV export…")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        ),
        "Accept": "text/csv,application/csv;q=0.9,*/*;q=0.8",
    }

    r = requests.get(URL, timeout=30, headers=headers)
    r.raise_for_status()
    return r.text

def main():
    csv_text = fetch_ntsb()

    df = pd.read_csv(StringIO(csv_text), low_memory=False)

    df.to_csv("data/ntsb_accidents.csv", index=False)
    print("[NTSB] Saved data/ntsb_accidents.csv")

if __name__ == "__main__":
    main()
