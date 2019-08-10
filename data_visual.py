from matplotlib import pyplot as plt
import pandas as pd

#x=[1,2,3,4,5,6,7,8,9,10]
#y=[1,3,5,6,7,8,9,10,13,17]
#z=[2,4,6,8,10,11,12,14,16,20]

#导入外部数据
data1=pd.read_csv('sample_data.csv') 

print(data1)
print(type(data1))

#选取表格中某个数据
number=data1.column_b.iloc[8]
number2=data1.iloc[3,1]

print(number)
print(number2)
#plt.plot(x,y,'x')
#plt.plot(x,z,'o')
#plt.legend(['y legend','z legend'])

#plt.xlabel('x')
#plt.ylabel('y and z')
#plt.title('Two plots')

#plt.show()


