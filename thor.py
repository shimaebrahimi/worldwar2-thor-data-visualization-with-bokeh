from turtle import color
import pandas as pd
from bokeh.plotting import figure,output_file,show,save
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
output_file('thor.html')
df=pd.read_csv('thor_wwii.csv').sample(500)
dfsource=ColumnDataSource(df)
p=figure()
p.circle(source=dfsource,x='AC_ATTACKING',y='TOTAL_TONS',color='red',size='TONS_IC')
p.title='عملیات هوایی جنگ جهانی دوم'
p.xaxis.axis_label='تعداد نیروهای هوایی'
p.yaxis.axis_label='حجم انفجار'
h=HoverTool()
h.tooltips=[
    ('تاریخ حمله','@MSNDATE'),
    ('نیروی هوایی','@AIRCRAFT_NAME'),
    ('کشور اعزام کننده','@COUNTRY_FLYING_MISSION')
]
p.add_tools(h)
save(p, "thor.html", title="thor")
show(p)
