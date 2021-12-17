# 2 Вариант
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import argparse
import math

from matplotlib import style
style.use('ggplot')

parser = argparse.ArgumentParser(description='main')
parser.add_argument('-quantity', dest='param_quantity', default=100, type=int)
args = parser.parse_args()

values = []
for i in range(100):
    values.append(np.random.rand())

values = list(np.sort(values))
# np.sort(a) равносильно вызову метода a.sort(), но в отличие от функции данный метод не возвращает копию,
# а меняет исходный массив

df = pd.DataFrame({'cos': map(math.cos, values), 'tang': map(math.tanh, values)})
df.index = values

# print(values)
# print(df)

plt.scatter(df.index, df['cos'], color='violet')
plt.scatter(df.index, df['tang'], color='aqua')

plt.show()

"""
Если плотность вероятности ϕ(х) есть величина постоянная на определенном промежутке [a,b], 
то закон распределения называется равномерным. 
"""


