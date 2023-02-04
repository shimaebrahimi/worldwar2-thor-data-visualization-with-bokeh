from datetime import datetime
from turtle import color
import pandas as pd
from bokeh.plotting import show,figure,output_file
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral4
output_file('thordate.html')
data=pd.read_csv('thor_wwii.csv')
data['MSNDATE']=pd.to_datetime(data['MSNDATE'],format='%m/%d/%Y')
dg=data.groupby('MSNDATE')['TOTAL_TONS','TONS_FRAG','TONS_IC','TONS_HE'].sum()
ds=ColumnDataSource(dg)
p=figure(x_axis_type='datetime')
# p.vbar_stack(source=ds,x='MSNDATE',color=Spectral4,width=0.7,stackers=['TOTAL_TONS','TONS_FRAG','TONS_IC','TONS_HE'],legend=['میزان تسحیلات','میزان قطعات','میزان اشتعال زا','مواد منفجره قوی'])
p.line(x='MSNDATE',y='TOTAL_TONS',source=ds,color='red',line_width=2,legend='میزان کل انفجارها')
p.line(x='MSNDATE',y='TONS_FRAG',source=ds,color='blue',line_width=2,legend='میزان کل قطعات')
p.line(x='MSNDATE',y='TONS_IC',source=ds,color='green',line_width=2,legend='میزان کل اشتعال زا')
p.line(x='MSNDATE',y='TONS_HE',source=ds,color='yellow',line_width=2,legend='میزان کل مواد قوی')
p.legend.click_policy='hide'
show(p)