from flask import Flask, render_template, request, flash
from scraper_requests import scrape_headlines
from scraper_selenium import scrape_with_selenium

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def index():
    headlines = []
    url = ""
    scraper_type = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        scraper_type = request.form.get("scraper")

        if not url:
            flash("❌ Please enter a valid URL", "error")
        else:
            if scraper_type == "requests":
                headlines = scrape_headlines(url, pages=1)
            elif scraper_type == "selenium":
                headlines = scrape_with_selenium(url)

    return render_template(
        "index.html",
        headlines=headlines,
        url=url,
        scraper_type=scraper_type
    )

if __name__ == "__main__":
    app.run(debug=True)
