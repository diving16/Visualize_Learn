import matplotlib.pyplot as plt


x_1=[1,3,5]
y_1=[4,5,6]
x_2=[2,4,6]
y_2=[7,2,6]

plt.xlabel('id')
plt.ylabel('rank')
plt.title('Performance')

plt.bar(x_1,y_1,label='2018',color='orange')
plt.bar(x_2,y_2,label='2019',color='c')
plt.legend()
plt.show()