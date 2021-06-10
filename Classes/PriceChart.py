import numpy as np
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
import plotly.graph_objects as go

from GEApp.ItemView.ItemPriceChanges import ItemPriceChanges

class PriceChart:
    def Chart(self, id, timefilter):
        chartchanges = ItemPriceChanges.PriceChanges(timefilter, id)

        my_plot_div = plot({"data": [go.Scatter(x=chartchanges['date'], y=chartchanges['dailyvalue'], fillcolor='red', line=dict(color='gold')),
                                     go.Scatter(x=chartchanges['date'], y=chartchanges['averagevalue'], fillcolor='red', line=dict(color='silver'))],
                            "layout": go.Layout(margin=go.layout.Margin(l=0, r=0, b=0, t=0), xaxis=dict(showgrid=False, fixedrange=True, tickfont=dict(color='white')), yaxis=dict(fixedrange=True, tickmode='array', tickfont=dict(color='white'), showticklabels=True, showgrid=True), showlegend=False, height=500, paper_bgcolor='rgb(104,187,227)', plot_bgcolor='rgb(104,187,227)')},
                            output_type='div', config=dict(displayModeBar=False))
        return my_plot_div
