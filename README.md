# Stock News Alert System 🚀

A Python project that monitors a specific stock's daily price changes and sends news alerts via SMS if the stock experiences a significant change.  

This example tracks **Tesla Inc (TSLA)**.

---

## Features

- Fetches daily stock prices using the [Alpha Vantage API](https://www.alphavantage.co/).
- Calculates the percentage difference between yesterday’s and the day before yesterday’s closing prices.
- If the change is greater than **5%**, fetches the top 3 news articles related to the company from [NewsAPI](https://newsapi.org/).
- Sends news alerts via SMS using [Twilio](https://www.twilio.com/).

---

## Requirements

- Python 3.x  
- `requests` library  
- `twilio` library  

Install dependencies via pip:

```bash
pip install requests twilio
