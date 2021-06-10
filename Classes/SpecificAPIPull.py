import requests

from GEApp.Classes.PriceChart import PriceChart


# noinspection PyRedundantParentheses
class SpecificAPIPull:
    def PullItem(self, id, filter):
        response = requests.get(
            "https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={}".format(id)).json()

        if(response['item'] != 0):
            detailPlaceholder = response['item']

            itemDetails = []
            print(detailPlaceholder['name'])

            # Keeping a record of the price with 'k' or 'm' in it
            actualpricePlaceholder = detailPlaceholder['current']['price']
            todaypricechangePlaceholder = detailPlaceholder['today']['price']

            # Change price if it has 'b' in it and replace it x1000000
            # Change price if it has 'b' in it and replace it x1000
            # Change price if is has 'k in it
            if('m' in str(detailPlaceholder['current']['price'])):
                detailPlaceholder['current']['price'] = float(str(detailPlaceholder['current']['price']).replace('m', '')) * 1000
            elif('k' in str(detailPlaceholder['current']['price'])):
                detailPlaceholder['current']['price'] = float(str(detailPlaceholder['current']['price']).replace('k', ''))
            elif('b' in str(detailPlaceholder['current']['price'])):
                detailPlaceholder['current']['price'] = float(str(detailPlaceholder['current']['price']).replace('b', '')) * 1000000

            if('m' in str(detailPlaceholder['today']['price'])):
                detailPlaceholder['today']['price'] = float(str(detailPlaceholder['today']['price']).replace(',', '.').replace('- ', '-').replace('m', '')) * 1000
            elif('k' in str(detailPlaceholder['today']['price'])):
                detailPlaceholder['today']['price'] = float(str(detailPlaceholder['today']['price']).replace(',', '.').replace('- ', '-').replace('k', ''))
            elif('b' in str(detailPlaceholder['today']['price'])):
                detailPlaceholder['today']['price'] = float(str(detailPlaceholder['today']['price']).replace(',', '.').replace('- ', '-').replace('b', '')) * 1000000

            todaychangepercent = '0'

            # Get the $ for todays change
            if(detailPlaceholder['today']['price'] is not 0):
                todaychangepercent = str(round(float(str(detailPlaceholder['current']['price']).replace(',', '.').replace('- ', '-')) / float(str(detailPlaceholder['today']['price']).replace(',', '.').replace('- ', '-'))))

            # Add + and %
            if(float(todaychangepercent) > 0):
                todaychangepercent = "+" + todaychangepercent + "%"
            else:
                todaychangepercent = todaychangepercent + "%"

            # Get the change in gold change
            day30change = round(float(str(detailPlaceholder['current']['price']).replace(',', '.')) * 1000 * float(str(detailPlaceholder['day30']['change']).replace(',', '.').replace('+', '').replace('%', '')) / (100 + float(str(detailPlaceholder['day30']['change']).replace(',', '.').replace('+', '').replace('%', ''))))
            day30change = '{:,.0f}'.format(day30change)

            day90todaychange = round((float(str(detailPlaceholder['current']['price']).replace(',', '.')) * 1000 * float(str(detailPlaceholder['day90']['change']).replace(',', '.').replace('+', '').replace('%', ''))) / (100 + float(str(detailPlaceholder['day90']['change']).replace(',', '.').replace('+', '').replace('%', ''))))
            day90todaychange = '{:,.0f}'.format(day90todaychange)

            day180todaychange = round((float(str(detailPlaceholder['current']['price']).replace(',', '.')) * 1000 * float(str(detailPlaceholder['day180']['change']).replace(',', '.').replace('+', '').replace('%', ''))) / (100 + float(str(detailPlaceholder['day180']['change']).replace(',', '.').replace('+', '').replace('%', ''))))
            day180todaychange = '{:,.0f}'.format(day180todaychange)

            an_item = dict(itemid=int(id), name=detailPlaceholder['name'], members=detailPlaceholder['members'], icon=detailPlaceholder['icon_large'], desc=detailPlaceholder['description'],
                           currentprice=detailPlaceholder['current']['price'], todaypricechange=todaypricechangePlaceholder, day30=detailPlaceholder['day30']['change'],
                           day90=detailPlaceholder['day90']['change'], day180=detailPlaceholder['day180']['change'], todaychangepercent=todaychangepercent, day30change=day30change,
                           day90change=day90todaychange, day180change=day180todaychange, actualprice=actualpricePlaceholder, filterselected=filter)
            itemDetails.append(an_item)

        return itemDetails

    # Price calculations
    # x = currentprice * increase / 100 + increase
    # x = 1643 * 2 / 98 = 33.53