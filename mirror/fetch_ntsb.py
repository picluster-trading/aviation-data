import asyncio
from playwright.async_api import async_playwright
import pandas as pd

RESULTS_URL = "https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx"
OUTPUT = "data/ntsb_accidents.csv"

async def fetch_ntsb_csv():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("[NTSB] Loading results/help page…")
        await page.goto(RESULTS_URL, timeout=120000, wait_until="networkidle")

        # This link downloads ALL records as a delimited text file
        print("[NTSB] Waiting for 'Download All (Text)' link…")
        download_link = page.get_by_text("Download All (Text)", exact=True)
        await download_link.wait_for(timeout=120000)

        print("[NTSB] Clicking 'Download All (Text)'…")
        async with page.expect_download() as download_info:
            await download_link.click()

        download = await download_info.value
        path = await download.path()

        print("[NTSB] Reading downloaded delimited text…")
        # NTSB “text” format is pipe-delimited with spaces around the pipe
        df = pd.read_csv(
            path,
            sep=r"\s*\|\s*",
            engine="python",
            dtype=str,
        )

        df.to_csv(OUTPUT, index=False)
        print(f"[NTSB] Saved {OUTPUT}")

        await browser.close()

def main():
    asyncio.run(fetch_ntsb_csv())

if __name__ == "__main__":
    main()
