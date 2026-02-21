import requests                                                          # used best for browse APIs
from send_email import send_email


api_key = "668b9a11297b46e098cf50185326b7a7"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2026-01-21&sortBy="
       "publishedAt&apiKey=668b9a11297b46e098cf50185326b7a7")

request = requests.get(url)                                              # get method
content = request.json()                                                 # .text function shows data in str \for dict. Json

body =""
for article in content["articles"]:
    if article["title"]is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] +2*"\n"
                                                                          # Now we can extract data with the help of debugger
                                                                          # and we see strings and keys like title, author,description
body = body.encode("utf-8")
send_email(body)
