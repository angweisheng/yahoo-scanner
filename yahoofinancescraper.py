import requests
import bs4
import time



news = [10]
latest_news = [10]


def scrape():
    result = requests.get("https://sg.finance.yahoo.com/topic/latestnews")
    soup = bs4.BeautifulSoup(result.text, "lxml")

    for item in soup.find_all(attrs={'class': 'Mb(5px)'}):
        for link in item.find_all('a'):
            grab = "https://sg.finance.yahoo.com" + link.get('href')
            
            
            news.append(grab)
            del news[1:]

        

            
def sort():
    latest_news[0] = news[0]
    

def deliver():
    print(news[0])
    '''print(latest_news)'''


'''def delivery():   
    while True:
        del news[:]
        scrape()

        if news != latest_news:
            sort()
            deliver()
            
        else:
            pass
        
        time.sleep(5)

delivery()'''
