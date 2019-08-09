import matplotlib.pyplot as plt

x=[1,2,5,7,8,4,6,7,9,10,13]
y=[60,67,64,70,89,60,90,100,8,14,15]

plt.scatter(x,y,label='scatter_plot',color='b',marker='x',s=500)

plt.xlabel('x')
plt.ylabel('y')
plt.title('A scatter plot')
plt.legend()

plt.show()