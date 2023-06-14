from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains, Keys
from bs4 import BeautifulSoup
import requests
import re


DoStayEat = []  # 0-9 Do, 10-19 Stay, 20-29 Eat


def scrapperFuncN(placeName):
    opt = Options()
    opt.add_argument("--headless=new")
    # Move the scraping code here
    url = f'https://www.tripadvisor.com/Search?q={placeName}'
    PATH = "F:\Selenium\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(PATH), options=opt)
    actions = ActionChains(driver)
    driver.get(url)
    time.sleep(10)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')

    link_extraction = str(
        soup.find('div', class_='ui_columns is-mobile result-content-columns'))

    rest = ''
    for index in range(117, len(link_extraction)):
        if (link_extraction[index] == '\''):
            break
        rest = rest + link_extraction[index]
    finalLink = f"https://www.tripadvisor.com/{rest}"
    print(finalLink)
    driver.get(finalLink)
    html_content1 = driver.page_source
    bigSoup = BeautifulSoup(html_content1, 'lxml')

    doStayEat_tags = bigSoup.find_all('div', class_='keSJi FGwzt ukgoS')
    for tags in doStayEat_tags:
        DoStayEat.append(tags.text)
    Do = []
    Eat = []
    Stay = []
    eat_price = []
    stay_price= []
    ratings = []
    image_links = []
    Do=DoStayEat[0:10]
    Stay=DoStayEat[10:20]
    Eat=DoStayEat[20:30]
    
    stay_price_tags = bigSoup.find_all('div', class_='biGQs _P fiohW fOtGX')
    eat_price_tags = bigSoup.find_all('div', class_='biGQs _P pZUbB hmDzD') 
    ratings_tags = bigSoup.find_all('div', class_='jVDab o W f u w JqMhy')
    image_tags = bigSoup.find_all('div', class_='hOjcA _T w')
    
    for tag in stay_price_tags:
        tag_content = str(tag.text)
        price = ''
        for i in range(6,len(tag_content)):
            if tag_content[i] == '/' or tag_content[i]=='p':
                break
            if tag_content[i]==',':
                continue
            price += tag_content[i]
        stay_price.append(int(price))

    for tag in eat_price_tags:
        element = ''
        span_tag = str(tag.span)
        for index in range(18,len(span_tag)):
            if span_tag[index]=='\"':
                break
            element += span_tag[index]
        eat_price.append(element)

    new_eat_price=[]
    i=0
    while(eat_price[i]==''):
        i+=1
    for j in range(i,i+10):
        new_eat_price.append(eat_price[j]) 
    #print("eat price: ",new_eat_price)
    
    #4.5 of 5 bubbles. 2,702 reviews
    ratings_pattern = '[0-9].[0-9]+ of [0-9] bubbles. .+ reviews'

    for tag in ratings_tags:
        element = ''
        each_tag = str(tag)
        search_result = str(re.search(ratings_pattern,each_tag))
        # print(each_tag)
        for index in range(40,len(search_result)):
            if search_result[index]=='\'':
                break
            element += search_result[index]
            new_element = element.replace('bubbles','stars')
        ratings.append(new_element)

    DoRatings = ratings[0:10]
    StayRatings = ratings[10:20]
    EatRatings = ratings[20:30]


    for tag in image_tags:
        element = ''
        image_tag = str(tag)
        startIndex = image_tag.find('https://')
        for index in range(startIndex,len(image_tag)):
            if image_tag[index]==' ':
                break
            element += image_tag[index]
        image_links.append(element)
    #First 30 elements of the list image_links are the do,stay,eat image links        

    
    driver.quit()
    return Do,Stay,Eat,new_eat_price,stay_price,ratings,image_links