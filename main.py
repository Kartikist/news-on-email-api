import requests 

api_key = "a36aaf886fb44ed8b954610544254aa7"
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-09-23&sortBy=publishedAt\
        &apiKey=a36aaf886fb44ed8b954610544254aa7'
    # api key = a36aaf886fb44ed8b954610544254aa7

request = requests.get(url)
content = request.json()
for article in content['articles']:
    print(article['title'])
    print(article['description'])

