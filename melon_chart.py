from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

csv_t = []
def temp(start_,end_):
    driver = webdriver.Chrome()
    for i in range(start_,end_):
        cnt = 0
        driver.get('https://www.melon.com/chart/month/index.htm')
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[3]/div').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[3]/div/div/dl/dd[2]/a').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/div/h4[2]/a').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/div/div/div[3]/div[1]/ul/li['+str(i)+']/span/label').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/div/div/div[5]/div[1]/ul/li[2]/span/label').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/button/span/span').click()
        time.sleep(0.5)

        id = driver.find_elements_by_class_name('like')
        
        title_temp = []
        artist_temp = []
        like_temp = []
        id_temp = []
        lyric_temp = []
        genre_temp = []
        date_temp = []

        for j in id:
            id_ = j.get_attribute('data-song-no')
            id_temp.append(id_)
            id_temp = id_temp[:50]
        for j in id_temp:
            driver.get('https://www.melon.com/song/detail.htm?songId='+j)
            lyric = driver.find_element_by_class_name('wrap_lyric')
            lyric_temp.append(lyric.text)
            lyric_temp = lyric_temp[:50]
            artist = driver.find_element_by_class_name('artist')
            artist_temp.append(artist.text)
            artist_temp = artist_temp[:50]
            title = driver.find_element_by_class_name('song_name')
            title_temp.append(title.text)
            title_temp = title_temp[:50]
            like = driver.find_element_by_class_name('cnt')
            like_temp.append(like.text)
            like_temp = like_temp[:50]
            genre = driver.find_element_by_css_selector('#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(6)')
            genre_temp.append(genre.text)
            genre_temp = genre_temp[:50]
            date = driver.find_element_by_css_selector('#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(4)')
            date_temp.append(date.text)
            date_temp = date_temp[:50]


        csv_t.append([[i,str(i)+'월'+str(p+1)+'등',title_temp[p],artist_temp[p],like_temp[p],(lyric_temp[p]).replace('\n',' '),genre_temp[p],date_temp[p]] for p in range(len(title_temp))])


st = int(input('시작월을 입력해주세요 : '))
en = int(input('끝월을 입력해주세요 : '))

temp(st,en+1)

import pandas as pd
import numpy as np

t = [j for i in range(len(csv_t)) for j in csv_t[i]]

df = pd.DataFrame(t,columns=['month','ranking','title','artist','like','lyric','genre','date'])
print(df)
df.to_csv('melon_chart.csv',index=False)
