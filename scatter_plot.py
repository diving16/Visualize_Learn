import matplotlib.pyplot as plt

x=[1,2,5,7,8,4,6,7,9,10,13]
y=[60,67,64,70,89,60,90,100,8,14,15]
month=[1,2,3,4,5,6,7,8,9,10,11,12]

plt.scatter(x,y,label='scatter_plot',color='b',marker='x',s=500)
A=[1,2,3,4,5,6,7,8,9,10,11,12]
B=[10,20,30,40,50,60,70,80,90,100,110,120]
C=[200,190,180,170,160,150,140,130,120,110,100,90]
D=[50,60,49,50,50,50,50,50,50,50,50,50]

plt.xlabel('x')
plt.ylabel('y')
plt.title('A scatter plot')

plt.show()
