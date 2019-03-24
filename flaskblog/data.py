from pyecharts import Bar
from pyecharts import Pie

from pyecharts import configure

configure(global_theme='vintage')

def piechart(df,col):
    attr = list(df[col].value_counts().index)
    v1 = list(df[col].value_counts().values)
    title = 'Portion about '+col
    pie = Pie(title)
    pie.add("", attr, v1, is_label_show=True)
    return pie
