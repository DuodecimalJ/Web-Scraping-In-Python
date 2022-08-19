import requests
from bs4 import BeautifulSoup
import os

resource_path = './res'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index9506.html'

page_number = 9506
while page_number>= 9505:
    url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page_number)


    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
# print(soup.prettify())

    article_title_html = soup.select('div[class="title"]')


    for each_article in article_title_html:
        if each_article.a != None:
            print(each_article.a.text)
            print('https://www.ptt.cc' + each_article.a['href'])

            article_url = 'https://www.ptt.cc' + each_article.a['href']
            article_text = each_article.a.text

            # Propose an URL request
            article_res = requests.get(article_url)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')

            #  Announce a change about the string
            article_content = article_soup.select('div#main-container')[0].text
            # print(article_content)
            with open(r'%s/%s.txt' %(resource_path, article_text), 'w' , encoding='utf-8') as w:
                w.write(article_content)








    page_number -=1











