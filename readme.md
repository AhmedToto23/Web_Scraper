Advanced Web Scraper
A robust Flask-based web application that allows users to extract headlines and content from any website. This tool provides a dual-engine approach to handle both lightweight static pages and complex, JavaScript-heavy dynamic sites.

🚀 Features
Universal Scraping: Extract content from any user-defined URL.

Dual Scraping Engines:

Static: Powered by Requests + BeautifulSoup4 for speed and efficiency.

Dynamic: Powered by Selenium to handle JavaScript-rendered content.

Clean Web UI: A modern, responsive interface to view results.

Intelligent Parsing: Automatically targets key content tags (<h1>, <h2>, <h3>).

Robust Error Handling: Managed alerts for network timeouts, invalid URLs, and parsing failures.

Pagination Support: Included for the Requests-based scraper to handle multi-page results.

📂 Project Structure
Plaintext

advanced-web-scraper/
│
├── app.py                 # Main Flask application logic
├── scraper_requests.py    # Static scraping module (Requests + BS4)
├── scraper_selenium.py    # Dynamic scraping module (Selenium)
├── requirements.txt       # Project dependencies
│
├── templates/
│   └── index.html         # Frontend HTML template
└── static/
    └── style.css          # Custom CSS styling
🛠️ Requirements
Python: 3.7+

Browser: Google Chrome installed.

Driver: ChromeDriver (Must match your installed Chrome version).

⚙️ Installation
Clone the repository.

pip install -r requirements.txt
Setup ChromeDriver: Ensure chromedriver is in your system PATH or placed in the project root.

💻 Usage
Launch the Flask server:


python app.py
Access the Dashboard: Open http://127.0.0.1:5000 in your web browser.

Scrape a Site:

Enter the target URL (e.g., https://www.bbc.com/news).

Select Method: Choose Requests for standard news sites or Selenium for sites that load content as you scroll or wait.

View Results: The extracted headlines will appear in a structured list.

🔧 Optional Enhancements
[ ] Export Data: Add functionality to download results as .csv or .json.

[ ] Database Integration: Store history using SQLite or PostgreSQL.

[ ] Authentication: Secure the dashboard with a login system.

[ ] Live Updates: Implement WebSockets (Flask-SocketIO) for real-time scraping progress.


🙏 Acknowledgements
BeautifulSoup Documentation

Requests: HTTP for Humans

Selenium Python Bindings

Flask Web Framework


👤 Author

Ahmed Toto
