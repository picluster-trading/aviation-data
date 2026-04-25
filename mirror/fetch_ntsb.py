import asyncio
from playwright.async_api import async_playwright
import pandas as pd

NTSB_URL = "https://www.ntsb.gov/Pages/AviationQuery.aspx"

OUTPUT = "data/ntsb_accidents.csv"

async def fetch_ntsb_csv():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("[NTSB] Loading page…")
        await page.goto(NTSB_URL, timeout=120000)

        print("[NTSB] Waiting for Download CSV button…")
        await page.wait_for_selector("a#downloadCsv", timeout=120000)

        print("[NTSB] Clicking Download CSV…")
        async with page.expect_download() as download_info:
            await page.click("a#downloadCsv")

        download = await download_info.value
        path = await download.path()

        print("[NTSB] Reading downloaded CSV…")
        df = pd.read_csv(path, low_memory=False)

        df.to_csv(OUTPUT, index=False)
        print(f"[NTSB] Saved {OUTPUT}")

        await browser.close()

def main():
    asyncio.run(fetch_ntsb_csv())

if __name__ == "__main__":
    main()
