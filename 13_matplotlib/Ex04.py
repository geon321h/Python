'''
Created on 2024. 8. 13.

@author: SIST221
'''
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt

font_location='c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

idx = ['국어', '영어', '수학']
col = ['웬디', '슬기', '조이']

df = DataFrame([[40, 50, 50], [70, 50, 20], [20, 20, 20]], \
               index=idx,
               columns=col)

print('df:\n',df)


#df.plot(kind='bar')
#df.plot.bar()
#df.plot.barh()
df.plot.barh(stacked=True)
plt.show()

print()









