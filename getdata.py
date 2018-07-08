# import libraries
import requests
import datetime
from bs4 import BeautifulSoup

class day:
    """A class containing 1 day of weather"""
    def __init__(self, date, timeframe):
        self.date = date
        self.timeframe = timeframe
        self.table = self.getTable(date)
        self.data = []

        self.processTable(self.table, self.data)

    def getTable(self, date):
        url = "https://www.wunderground.com/hourly/us/mn/victoria/date/" + date + "/KMNVICTO2?cm_ven=localwx_hour"
        page = requests.get(url)
        #parse HTML
        soup = BeautifulSoup(page.content, 'html.parser')
        #find the table
        table = soup.select("#hourly-forecast-table tr")
        return table

    def processTable(self, table, data):
        for row in table:
            cells = row.findAll('td')
            if len(cells) > 0:
                hour = {"time":0, "temp":0, "wind":0, "condition":0}

                hour['time'] = cells[0].text.encode('utf-8').strip()
                hour['condition'] = cells[1].text.encode('utf-8').strip().split("\n")[0]
                hour['temp'] = cells[2].text.encode('utf-8').strip().split(" \xc2\xb0F")[0]
                hour['wind'] = cells[9].text.encode('utf-8').strip()

                print hour['temp']

                data.append(hour)
        print data



day(str(datetime.date.today()), 3)
