from flask import Flask, render_template, send_from_directory, request
import os

from GEApp.Classes.APIDriver import APIDriver
from GEApp.Classes.ItemModel import ItemModel
from GEApp.Classes.DebugTime import DebugTime
from GEApp.Classes.PageNumberCreation import PageNumberCreation
from GEApp.ItemView.itemview import item_view

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.

app = Flask(__name__)
app.register_blueprint(item_view, url_prefix="")


# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.ico')


@app.route("/about", methods=['GET', 'POST'])
def about():
    # Render the about page
    titleMsg = APIDriver()

    # Get the name of the searched item
    itemname = request.form.get('variable')

    print("HOW MANY TIMES IS THIS BEING CALLED\n")
    return render_template("about.html", title=titleMsg.call_api(1, itemname))


@app.route('/', methods=['GET', 'POST'])
def index():
    # Index of the website
    mds = ItemModel()

    # Redirection
    template = 'index.html'

    # Get the name of the searched item
    itemname = request.form.get('variable')

    # Receive selected data from HTML
    receivedData = str(request.form.get('pagenumber')).split(',', maxsplit=1)

    if receivedData is not None:
        page = receivedData[0].replace('(', '').replace(',', '')

    if len(receivedData) > 1:
        itemname = receivedData[1].replace('\'', '').replace(')', '')[1:]

    # Render the about page
    titleMsgAbout = APIDriver()

    # Used in case I need to change the page
    if itemname:
        template = 'index.html'

    # Number of pages and passable item
    pageNumbers = titleMsgAbout.call_api(page, itemname)
    passableItem = 'No item found'
    passableData = 'No item found'

    if (pageNumbers):
        pageNumbers = titleMsgAbout.call_api(page, itemname)[0]['pages']
        passableData = PageNumberCreation.Create(itemname, pageNumbers)
        passableItem = passableData['name']

    DebugTime.PrintMessage("INDEX.html LOADED")
    DebugTime.PrintMessage('PAGE SELECT {} SEARCH SELECTED {}'.format(page, itemname))
    DebugTime.PrintMessage('This is what PageNumberCreation looks like: {}'.format(passableItem))

    return render_template(template, headers=mds.headers, title=titleMsgAbout.call_api(page, itemname),
                           passableData=itemname,
                           pageNumber=passableData)


if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449, debug=True)
