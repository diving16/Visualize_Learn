from matplotlib import pyplot as plt
import pandas as pd

data2=pd.read_csv('countries.csv')

China_filter=data2.country=='China'
China_data=data2[China_filter]

Brazil_filter=data2.country=='Brazil'
Brazil_data=data2[Brazil_filter]

Japan_filter=data2.country=='Japan'
Japan_data=data2[Japan_filter]

Sweden_filter=data2.country=='Sweden'
Sweden_data=data2[Sweden_filter]

print(China_data)
print(Brazil_data)
print(Japan_data)
print(Sweden_data)

#改变单位，就可以不显示科学记数法
#plt.plot(China_data.year,China_data.population/10**8)
#plt.plot(Brazil_data.year,Brazil_data.population/10**8)
#plt.plot(Japan_data.year,Japan_data.population/10**8)
#plt.plot(Sweden_data.year,Sweden_data.population/10**8)

#plt.xlabel('Year')
#plt.ylabel('Population')
#plt.title('Countries\' Population')
#plt.legend(['China','Brazil','Japan','Sweden'])

#经过上面的画图，可以发现除了中国之外的三个国家数值较低，效果不明显
#此时没必要将数据缩小
plt.plot(China_data.year,
         China_data.population/China_data.population.iloc[0])
plt.plot(Brazil_data.year,
         Brazil_data.population/Brazil_data.population.iloc[0])
plt.plot(Japan_data.year,
         Japan_data.population/Japan_data.population.iloc[0])
plt.plot(Sweden_data.year,
         Sweden_data.population/Sweden_data.population.iloc[0])

plt.xlabel('Year')
plt.ylabel('Population Growth')
plt.title('Countries\' Population')
plt.legend(['China','Brazil','Japan','Sweden'])
plt.show()

