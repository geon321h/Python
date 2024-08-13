'''
Created on 2024. 8. 13.

@author: SIST221
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

font_location='c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']

filename = 'capital_area.csv'
df = pd.read_table(filename,sep='|', header=None, names=mycolumn)

result = df.groupby('영업소코드')[['2종교통량','3종교통량', '4종교통량', '5종교통량', '6종교통량']].sum()
print(result)

result.plot.bar()
plt.title('교통량 평균')
plt.ylabel('교통량',rotation=0)
plt.xticks(rotation=0)

plt.show()









