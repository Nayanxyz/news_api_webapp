import requests                                                          # used best for browse APIs
from send_email import send_email

topic = "tesla"
api_key = "668b9a11297b46e098cf50185326b7a7"                    #& separates url / used variable topic instead hard coded "tesla" using f string
url = (f"https://newsapi.org/v2/everything?q={topic}&"
       "from=2026-01-22&"
       "sortBy=publishedAt&"
       "apiKey=&"
       "language=en")

request = requests.get(url)                                              # get method
content = request.json()                                                 # .text function shows data in str \for dict. Json

body ="subject: Today`s news" + "\n"                                       #empty string // or add subject

for article in content["articles"][0:20]:                                # limit emails using slicing
    if article["title"]is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["url"] +"\n" + article["description"] +2*"\n"
                                                                          # Now we can extract data with the help of debugger
                                                                          # and we see strings and keys like title, author,description
body = body.encode("utf-8")                                               # converting mails to utf 8
send_email(body)
