from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import csv

#Connection au site Web : 

URL='https://www.amazon.com/s?k=ps5+games&crid=1KHNQ7L5O930&sprefix=ps5+games%2Caps%2C167&ref=nb_sb_noss_1'



headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6",
    "Upgrade-Insecure-Requests": "1",
    }



the_day =str(datetime.date.today())




page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

List_of_indexs=list(range(1,26,1))

header = ['Title', 'Price', 'Rating','Date']


Elements=[]



i=1

while i in List_of_indexs :
    try:
        div_Container =soup.find('div',{'data-index' : str(List_of_indexs[i-1])})
        div_title=div_Container.find('span',{'class':'a-text-normal'}).get_text()
        rating_container=div_Container.find('span',{'class':'a-icon-alt'}).get_text()
        rating=float(rating_container[0:3])
        price_whole=div_Container.find('span',{'class':'a-price-whole'}).get_text()
        price_fraction=div_Container.find('span',{'class':'a-price-fraction'}).get_text()
        price=float(str(price_whole)+str(price_fraction))
        temporary_list=[]
        temporary_list.append(div_title)
        temporary_list.append(price)
        temporary_list.append(rating)
        temporary_list.append(the_day)
        Elements.append(temporary_list)
        i+=1
    except:
        i+=1



print(Elements)
print(len(Elements))

with open(r'C:\Users\lazra\OneDrive\Bureau\TP Scraping\AmazonWebScraperDataset1.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for j in range(len(Elements)-1):
        writer.writerow(Elements[j])
    