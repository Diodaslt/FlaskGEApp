class PageNumberCreation:
    """ Create the page numbers """

    def Create(self, pagenumbers):
        pageList = {}

        # Create page button
        for x in range(1, pagenumbers + 1):
            pageList[x] = x

        itemlist = dict(name=self, pagenumber=pageList)

        return itemlist
