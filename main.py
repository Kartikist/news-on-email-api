import requests 
import send_email as m

api_key = "a36aaf886fb44ed8b954610544254aa7"
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-09-23&sortBy=publishedAt\
        &apiKey=a36aaf886fb44ed8b954610544254aa7'
    # api key = a36aaf886fb44ed8b954610544254aa7

mail = ''
request = requests.get(url)
content = request.json()
for article in content['articles']:
    if article['title'] is not None:
        mail = mail + article['title'] + '\n' + article['description'] + 2*'\n'

mail = mail.encode('utf-8')

m.send_email(message= mail)
   

    
    


