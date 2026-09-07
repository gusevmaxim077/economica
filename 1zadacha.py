import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

departaments = ['A','B', 'C', 'D', 'E']

before = np.array([120,135,110,150,130])
after = np.array([145,155,140,160,150])

df = pd.DataFrame ({'Отдел': departments, 'До внедрения': before, 'После внедрения': after})

df['Абсолютный прирост'] = df['После внедрения'] - df['До внедрения']
df['Относительный прирост, %'] = (df['Абсолютный прирост'] / df['До внедрения'] * 100)

mean_before = np.mean(before)
mean_after = np.mean(after)

print('=' * 60)
print('Оценка влияния информатизации')
print('=' * 60)
print(df.ro_string(index = False))

print('\nСредняя выработка до внедрения:', f'{mean_before:.2f} тыс. руб./чел.')
print('\nСредняя выработка после внедрения:', f'{mean_after:.2f} тыс. руб./чел.')

absolute growth = mean_after - mean_before
relative_growth = absolute_growth / mean before * 100

print(f'Средний абсолютный прирост:{absolute_growth:.2f} тыс. руб./чел.')
print(f'Средний относительный прирост:{relative_growth:.2f} тыс. руб./чел.')

t_stat, p_value = stats.ttest_rel(after, before)

print('\nПарный t-критерий Стьюдента')
print(f't-статистика: {t_stat:.4f}')
print(f'p-value: {p_value:.4f}')

alpha = 0.05

if p_value < alpha:
  print('Вывод: отвергаем нулевую гипотезу, рост производительности значим')
else:
  print('Вывод: не отвергаем нулевую гипотезу, рост производительности статистически значим.')

print('\nМедианная оценка')
print(f'Медиана до внедрения: {np.median(before):.2f}')
print(f'Медиана после внедрения: {np.median(after):.2f}')
print(f'Медиана до внедрения: {np.median(after) - np.median(before):.2f}')

plt.figure(figsize(8, 5))

x = np.arange(len(departments))
width = 0.35

plt.bar(x - width / 2, before, width, label = 'До внедрения', color = 'skyblue')
plt.bar(x - width / 2, after, width, label = 'После внедрения', color = 'orange')

plt.xlabel('Отделы')
plt.ylabel('Выработка, тыс. руб./чел.')
plt.title('Динамика производительности труда')
plt.xticks(x, departmnets)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show


                                  
