# 📰 Automated News Courier

A lightweight Python automation tool that dynamically fetches the latest news articles for a specified topic using the [NewsAPI](https://newsapi.org/) and delivers a formatted summary directly to your email inbox via SMTP.

## ✨ Features

- **Automated Data Retrieval:** Leverages the `requests` library to interface with NewsAPI and pull the top 20 most relevant articles based on keyword queries.
- **Smart Formatting:** Parses JSON responses to extract article titles, URLs, and descriptions, compiling them into a clean, readable email body.
- **Secure Delivery:** Utilizes `smtplib` and `ssl` to establish a secure, encrypted connection to Google's SMTP servers for safe email transmission.
- **UTF-8 Encoding:** Ensures compatibility across various email clients and special characters.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed and configured:

- **Python 3.x**
- **Requests Library:** `pip install requests`
- **NewsAPI Key:** Get a free API key from [NewsAPI.org](https://newsapi.org/).
- **Gmail App Password:** If using Gmail, you must generate an [App Password](https://myaccount.google.com/apppasswords) (standard account passwords will not work due to security protocols).

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nayanxyz/news_api_webapp.git
   cd automated-news-courier
   ```

2. **Install dependencies:**

```Bash
pip install requests
```
Configure your credentials:
Open the scripts and securely input your environment variables (API keys, email, and app password). Note: It is highly recommended to use a .env file instead of hardcoding credentials.

3. **Run the script:**

```Bash
python main.py
```

## ⚙️ Configuration
Topic: Modify the topic variable in main.py (currently set to "tesla") to track any subject of your choice.

Date Range: Adjust the from parameter in the API URL to filter news from a specific date.

Limit: The script currently slices the API response to the top 20 articles ([0:20]). You can modify this integer to increase or decrease email volume.
