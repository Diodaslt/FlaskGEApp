from flask import Blueprint, render_template, request, Markup

from GEApp.Classes.DebugTime import DebugTime

from GEApp.Classes.SpecificAPIPull import SpecificAPIPull
from GEApp.Classes.PriceChart import PriceChart

item_view = Blueprint('item_view', __name__, template_folder='templates', static_folder='static')

@item_view.route('/itemview',  methods=['GET', 'POST'])
def itemview():
    itempull = SpecificAPIPull()
    selecteditem = request.args.get('itemid')
    filter = request.args.get('filter')

    # Generate chart
    chart = PriceChart().Chart(filter, selecteditem)

    # Pull item by id
    itemd = itempull.PullItem(selecteditem, filter)

    DebugTime.PrintMessage('Selected item {}'.format(itemd))
    return render_template('itemview.html', itemdetails=itemd, chart=Markup(chart))