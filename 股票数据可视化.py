# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:21:46 2019

@author: KID
"""

import tushare as ts
import pyecharts as pe

df_qjd = ts.get_hist_data('000725')
df_qjd = df_qjd.iloc[::-1]
x = df_qjd.index.tolist()
y = df_qjd[['open', 'close', 'low', 'high']].values.tolist()

#df_qjd['ma5'] = df_qjd['close'].rolling(window=5).mean()
#df_qjd['ma10'] = df_qjd['close'].rolling(window=10).mean()
#df_qjd['ma20'] = df_qjd['close'].rolling(window=20).mean()

m5 = df_qjd['ma5'].tolist()
m10 = df_qjd['ma10'].tolist()
m20 = df_qjd['ma20'].tolist()


kline = pe.Kline('k线图', height=800, width=1500)
kline.add('日k线图', x, y,
         is_datazoom_show=True,
         datazoom_range=[70,90],
         tooltip_axispointer_type='cross',
         mark_point=['max', 'min'])

line = pe.Line('均线')
line.add('5日均线', x, m5)
line.add('10日均线', x, m10)
line.add('20日均线', x, m20)

overlap = pe.Overlap(height=850, width=1800)
overlap.add(kline)
overlap.add(line)


overlap.render('C:/Users/KID/Desktop/股票数据可视化.html')