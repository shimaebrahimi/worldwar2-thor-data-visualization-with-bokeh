from turtle import color, width
import pandas as pd
from bokeh.plotting import show,figure,output_file
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
output_file('thor3.html')
data=pd.read_csv('thor_wwii.csv')
data=data[data['COUNTRY_FLYING_MISSION'].isin(('GREAT BRITAIN','USA'))]
datagr=data.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS','TONS_FRAG','TONS_IC','TONS_HE'].sum()
ds=ColumnDataSource(datagr)
countries=ds.data['COUNTRY_FLYING_MISSION'].tolist()
p=figure(x_range=countries)
# cm=factor_cmap(field_name='COUNTRY_FLYING_MISSION',palette=Spectral4,factors=countries)
p.vbar_stack(source=ds,x='COUNTRY_FLYING_MISSION',width=0.7,color=Spectral3,stackers=['TONS_HE','TONS_IC','TONS_FRAG'],legend=['منفجره','آتش زا','قطعات'])
# h=HoverTool()
# h.tooltips=[
#     ('جمع','جمع مواد منفجره قوی @TONS_HE است و جمع مواد آتش زا @TONS_IC و جمع @TONS_FRAG است مواد پخش ')
# ]
# h.mode='vline'
# p.add_tools(h)
show(p)