from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_with_selenium(url):
    """Scrape headlines from dynamic sites using Selenium"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    headlines = []
    try:
        driver.get(url)
        time.sleep(3)  # wait for JS to render

        for el in driver.find_elements(By.TAG_NAME, "h1") + \
                  driver.find_elements(By.TAG_NAME, "h2") + \
                  driver.find_elements(By.TAG_NAME, "h3"):
            text = el.text.strip()
            if text and text not in headlines:
                headlines.append(text)
    finally:
        driver.quit()

    return headlines
