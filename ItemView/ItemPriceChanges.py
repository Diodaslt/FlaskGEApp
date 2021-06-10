import time

import requests
from datetime import datetime, timedelta

class ItemPriceChanges:
    def PriceChanges(self, timeframe):
        response = requests.get(
            "https://secure.runescape.com/m=itemdb_rs/api/graph/{}.json".format(self)).json()

        # Set up variables for 30, 90 and 180 days worth of data
        # Convert miliseconds
        date = [datetime.fromtimestamp(int(k)/1000).strftime('%Y-%m-%d %H:%M:%S') for k, v in response['daily'].items()]
        date30days = date[-30:]
        date90days = date[-90:]
        date180days = date[-180:]

        dailyvalue = [int(v) for k, v in response['daily'].items()]
        datevalue30days = dailyvalue[-30:]
        datevalue90days = dailyvalue[-90:]
        datevalue180days = dailyvalue[-180:]

        averagevalue = [int(v) for k, v in response['average'].items()]
        averagevalue30days = averagevalue[-30:]
        averagevalue90days = averagevalue[-90:]
        averagevalue180days = averagevalue[-180:]

        # Expect empty value
        if timeframe is None:
            timeframe = 180

        # Data filter
        if int(timeframe) is 30:
            date = date30days
            dailyvalue = datevalue30days
            averagevalue = averagevalue30days

        if int(timeframe) is 90:
            date = date90days
            dailyvalue = datevalue90days
            averagevalue = averagevalue90days

        if int(timeframe) is 180:
            date = date180days
            dailyvalue = datevalue180days
            averagevalue = averagevalue180days

        pricechange = dict(date=date, dailyvalue=dailyvalue, averagevalue=averagevalue)

        return pricechange