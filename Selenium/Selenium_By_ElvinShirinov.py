# First we need to import important libraries from the package, if you didn't  intall before please install them from the packages
from selenium import webdriver
import requests
import pandas as pd
import numpy as np
import re #regular expression
from bs4 import BeautifulSoup
import time

data1 = pd.DataFrame()
# Please replace the path to the Chrome web driver in the function below
driver = webdriver.Chrome(r'C:\Users\Baku\Downloads\chromedriver_win32\chromedriver')
from selenium.webdriver.chrome.options import Options
# Please replace the path to the Chrome web driver in the function below
executable_path = r'C:\Users\Baku\Downloads\chromedriver_win32\chromedriver'

chrome_options = Options()
# Please replace the path to the uBlock Origin browser extension in the function below
chrome_options.add_extension(r'C:\Users\Baku\.jupyter\uBlock-Origin.zip')

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
driver.get('https://hdtoday.tv')
driver.find_element("css selector", '#xheader_menu > ul.header_menu-list > li:nth-child(2) > a').click()
driver.switch_to.window(driver.window_handles[0])

# Here we are select hte page range, you can select any page number
for page_num in range(20, 100):
    try:
        url11 = driver.current_url +"?page="+str(page_num)

        driver.get(url11)

        all_links = []
        for link in BeautifulSoup(driver.page_source,features="html.parser").findAll('a'):
            all_links.append(link.get('href'))

        head = 'https://hdtoday.tv/'
        links = all_links[154:-16:2]

        for i in range(len(links)):

            main_url = head + links[i]

            page_inside = requests.get(main_url)
            html_1 = BeautifulSoup(page_inside.content, 'html.parser')

            movie_info = html_1.find_all('div', class_ = 'row')

            movie_info_name = html_1.find_all('h2', class_ = 'heading-name')

            movie_info_imdb = html_1.find_all('span', class_ = 'item mr-2')

            movie_info_1 = re.sub('<[^>]+>', '', str(movie_info)).replace('\n','').replace(' ','')
# Here we are getting the main data from the website:
            imdb = re.sub('<[^>]+>', '', str(movie_info_imdb)).replace('[','').replace(']','').replace('IMDB: ','')
            movie_name = re.sub('<[^>]+>', '', str(movie_info_name)).replace('[','').replace(']','')
            releasedate = movie_info_1[movie_info_1.find('Released')+9:movie_info_1.find("Genre")]
            genres = movie_info_1[movie_info_1.find('Genre')+6:movie_info_1.find("Casts")]
            casts = movie_info_1[movie_info_1.find('Casts')+6:movie_info_1.find("Duration")]
            duration = movie_info_1[movie_info_1.find('Duration')+9:movie_info_1.find("Country")-3]
            country = movie_info_1[movie_info_1.find('Country')+8:movie_info_1.find("Production")]

# Here we are creating the our dataset with that data from website
            data1 = data1.append({
               'Name':movie_name,
                'Release_Date':releasedate,
                'Genre':genres,
                'Cast':casts,
                'Duration':duration,
                'Country':country,
                'IMDB':imdb},ignore_index=True)

    except BaseException as error:
        print(error)

    data1['Duration'] = pd.to_numeric(data1['Duration'], errors='coerce')
    data1 = data1[data1['Duration'].notna()]

    # determining the name of the file
    file_name = '1MovieData.xlsx'

    # saving the excel
    data1.to_excel(file_name)
    #print(data1.head())




