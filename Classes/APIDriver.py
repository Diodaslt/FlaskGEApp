import requests

from GEApp.Classes.DebugTime import DebugTime
from GEApp.Classes.ItemModel import ItemModel

class APIDriver:
    """ Gets data for searchable item """
    def call_api(self, page, itemname):

        if(itemname and page):
            response = requests.get("https://secure.runescape.com/m=itemdb_rs/api/catalogue/search.json?page={0}&query={1}&simple=1".format(page, itemname)).json()

            DebugTime.PrintMessage("https://secure.runescape.com/m=itemdb_rs/api/catalogue/search.json?page={0}&query={1}&simple=1".format(page, itemname))

            # Initialize item model and clear it
            newList = ItemModel()
            newList.data.clear()

            if(response['page'] != 0):

                # check if the page exists
                DebugTime.PrintMessage('Length of {}'.format(len(response['results'])))

                # Create a placeholder
                itemPlaceholder = response['results']
                # Total number of pages worth of data in the json
                pageNumber = response['totalPages']
                items = []

                # Create a list of data
                for x in range(len(response['results'])):
                    an_item = dict(id=itemPlaceholder[x]['id'], icon=itemPlaceholder[x]['icon'], name=itemPlaceholder[x]['name'], member=itemPlaceholder[x]['members'],
                                   price=itemPlaceholder[x]['current']['price'], change=itemPlaceholder[x]['today']['price'], pages=pageNumber)
                    items.append(an_item)
                responseVar = items
            else:
                # Clear list if no items are found
                # and display message
                newList.data.clear()
                responseVar = "NO ITEM FOUND"
        else:
            responseVar = bool(0)
            DebugTime.PrintMessage(responseVar)

        return responseVar