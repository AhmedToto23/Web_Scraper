import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0)"
}

def scrape_headlines(url, pages=1):
    """Scrape headlines from a given URL using Requests + BS"""
    headlines = []

    for page in range(1, pages + 1):
        try:
            page_url = f"{url}?page={page}" if page > 1 else url
            response = requests.get(page_url, headers=HEADERS, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all h1, h2, h3 tags as potential headlines
            for tag in soup.find_all(["h1", "h2", "h3"]):
                text = tag.get_text(strip=True)
                if text and text not in headlines:
                    headlines.append(text)

        except requests.RequestException as e:
            print(f"Error scraping {page_url}: {e}")

    return headlines
