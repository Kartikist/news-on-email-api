import requests 
import send_email as m

api_key = "a36aaf886fb44ed8b954610544254aa7"
topic = 'zomato'
url = f'https://newsapi.org/v2/everything?q={topic}&from=2023-09-23&sortBy=publishedAt&apiKey=a36aaf886fb44ed8b954610544254aa7&language=en'
    # api key = a36aaf886fb44ed8b954610544254aa7

mail = ''
request = requests.get(url)
content = request.json()
for article in content['articles'][:1]:
    if article['title'] is not None:
        mail =  mail + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'
        

mail = "Subject: Today's news" +'\n' + mail
mail = mail.encode('utf-8')

m.send_email(message= mail)
   

    
    


