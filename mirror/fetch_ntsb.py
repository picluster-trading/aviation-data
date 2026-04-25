import requests
import pandas as pd
from io import StringIO

URL = "https://www.ntsb.gov/_layouts/15/NTSB.Aviation/DownloadCSV.aspx"

def fetch_ntsb():
    print("[NTSB] Fetching CSV export…")
    r = requests.get(URL, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return r.text

def main():
    csv_text = fetch_ntsb()

    df = pd.read_csv(StringIO(csv_text), low_memory=False)

    df.to_csv("data/ntsb_accidents.csv", index=False)
    print("[NTSB] Saved data/ntsb_accidents.csv")

if __name__ == "__main__":
    main()
