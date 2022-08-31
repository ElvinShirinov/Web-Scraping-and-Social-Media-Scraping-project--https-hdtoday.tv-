# First we need to import this libraries, if you don't have please download them from packages.
import requests
import pandas as pd
import numpy as np
import re #regular expression
from bs4 import BeautifulSoup

data = pd.DataFrame()
# Here We are select the pages range, you can select any page number
for pagenum in range(20,100):
    try:
        url = f'https://hdtoday.tv/movie?page={pagenum}'
        page = requests.get(url)
        html = BeautifulSoup(page.content, 'html.parser')

        all_links = []
        for link in html.findAll('a'):
            all_links.append(link.get('href'))

        head = 'https://hdtoday.tv'

        links = all_links[154:-16:2]

        for i in range(len(links)):

            main_url = head + links[i]

            page_inside = requests.get(main_url)
            html_1 = BeautifulSoup(page_inside.content, 'html.parser')

            movie_info = html_1.find_all('div', class_ = 'row')

            movie_info_name = html_1.find_all('h2', class_ = 'heading-name')

            movie_info_imdb = html_1.find_all('span', class_ = 'item mr-2')

            movie_info_1 = re.sub('<[^>]+>', '', str(movie_info)).replace('\n','').replace(' ','')
# Here We are gettting our main data from the website :
            imdb = re.sub('<[^>]+>', '', str(movie_info_imdb)).replace('[','').replace(']','').replace('IMDB: ','')
            movie_name = re.sub('<[^>]+>', '', str(movie_info_name)).replace('[','').replace(']','')
            releasedate = movie_info_1[movie_info_1.find('Released')+9:movie_info_1.find("Genre")]
            genres = movie_info_1[movie_info_1.find('Genre')+6:movie_info_1.find("Casts")]
            casts = movie_info_1[movie_info_1.find('Casts')+6:movie_info_1.find("Duration")]
            duration = movie_info_1[movie_info_1.find('Duration')+9:movie_info_1.find("Country")-3]
            country = movie_info_1[movie_info_1.find('Country')+8:movie_info_1.find("Production")]

            data = data.append({
               'Name':movie_name,
                'Release_Date':releasedate,
                'Genre':genres,
                'Cast':casts,
                'Duration':duration,
                'Country':country,
                'IMDB':imdb},ignore_index=True)
    except:
        continue

data['Duration'] = pd.to_numeric(data['Duration'],errors = 'coerce')
data = data[data['Duration'].notna()]
print (data)

# determining the name of the file
file_name = 'NewMovieData.xlsx'

# saving the excel
data.to_excel(file_name)
