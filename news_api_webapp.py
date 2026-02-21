import requests  # used best for browse APIs

api_key = "668b9a11297b46e098cf50185326b7a7"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2026-01-21&sortBy="
       "publishedAt&apiKey=668b9a11297b46e098cf50185326b7a7")

request = requests.get(url)  # get method
content = request.json()  # .text function shows data in str \for dict. Json

for article in content["articles"]:
    print(article["author"])  # Now we can extract data with the help of debugger
    print(article["title"])  # and we see strings and keys like title, author,description
