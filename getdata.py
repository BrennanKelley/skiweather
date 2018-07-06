# import libraries
import requests

page = requests.get("https://www.wunderground.com/hourly/us/mn/victoria/KMNVICTO2?cm_ven=localwx_hour")
#print page.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#table = soup.find("table", id='hourly-forecast-table')

#print table

table = soup.select("#hourly-forecast-table tr")


for t in table:
    cells = t.findAll('td')
    if len(cells) > 0:
        time = cells[0].text.encode('utf-8').strip()
        temp = cells[2].text.encode('utf-8').strip()
        wind = cells[9].text.encode('utf-8').strip()
        print "{0},  {1},  {2}".format(time,temp,wind)


# #for t in table:
# cells = table[2].findAll('td')
# print len(cells)
# if len(cells) > 0:
#     time = cells[0].text.encode('utf-8').strip()
#     temp = cells[2].text.encode('utf-8').strip()
#     wind = cells[9].text.encode('utf-8').strip()
#     print "{0},  {1},  {2}".format(time,temp,wind)
