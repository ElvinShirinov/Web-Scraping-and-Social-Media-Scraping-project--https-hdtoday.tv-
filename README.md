###Scrapy###

There are two spiders in the spiders folder. Number 1 and 2. The first spider scrapes the links of the movies in the homepage. 
The second one scrapes the details from each movie page.
To run the spiders correctly, please, follow the instructions below:
1. Open the whole Scrapy folder in your recommended software(VSCode, Pycharm)
2. Open terminal and go to the folder directory.
3. Run the code: scrapy crawl link_lists -O links.csv - this code will execute the first spider which will create 
and .csv file with links.
4. Now the code: scrapy crawl movies -o movies.csv - this code will execute the second spider which will scrape all the date 
and create a csv file.

###Selenium###
1. Download the folder named "Selenium"
2. Before executing the scrapping process, please ensure you have the "Chrome" web driver and the "uBlock Origin" browser extension on your machine.
3. To start the web scrapping process please open the "Selenium_By_ElvinShirinov.py".
4. Before running the python file, please change the paths to the "Chrome" web driver and the "uBlock Origin" browser extension with the paths to location where they're stored on your machine.
5. Finally, to execute the scrapping process, please run the "Selenium_By_ElvinShirinov.py" after making the changes to it from the previous step.
6. The results of the file execution can be obtained in the Excel file that gets created in the current folder.

###Soup###
1. Please download the folder named "Soup"
2. To execute the web scrapping process, please open and run the "Soup_By_ElvinShirinov.py" file
3. The results of the file execution can be obtained in the Excel file that gets created in the current folder.
