STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api=""
news_api=""
account_sid =""
auth_token = ""
twilio_number=""
send_to_number=""
import requests
from twilio.rest import Client
parameters_1={"apikey":stock_api,"function":"TIME_SERIES_DAILY","symbol":STOCK_NAME}
response=requests.get(STOCK_ENDPOINT,params=parameters_1)
data=response.json()
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
time_series=data["Time Series (Daily)"]
dates=list(time_series.keys())
yesterday=dates[0]
d_b_y=dates[1]
yesterday_closing_price=float(time_series[yesterday]["4. close"])
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday=float(time_series[d_b_y]["4. close"])
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=abs(float(yesterday_closing_price-day_before_yesterday))
up_down=None
if difference>0:
    up_down="⬆️"
else:
    up_down="⬇️"
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_dif=(difference/day_before_yesterday)*100
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_dif>5:
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    parameters={"apiKey":news_api,"q":COMPANY_NAME,"language": "en"}
    news_response=requests.get(NEWS_ENDPOINT,params=parameters)
    full_news=news_response.json()
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    news=full_news["articles"][:3]
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    publish_news=[{"title": article["title"],"description":article["description"]}for article in news]
#TODO 9. - Send each article as a separate message via Twilio.
    client=Client(account_sid,auth_token)
    for article in publish_news:
         message = client.messages.create(
             body=f'{STOCK_NAME}: {up_down}{percentage_dif:.2f}%\nHeadline: {article["title"]}\nBrief: {article["description"]}',
             from_=twilio_number,  # Your Twilio number
             to=send_to_number  # Your phone number
         )
         print(message.status)



