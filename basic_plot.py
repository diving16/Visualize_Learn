import matplotlib.pyplot as plt
x_1=[1,2,3,4,5,6,7]
y_1=[1,2,3,4,5,6,7]

x_2=[1,2,3,4,5,6,7]
y_2=[4,5,7,2,8,4,9]


plt.xlabel('id')
plt.ylabel('score')
plt.title('Evaluation\nids and scores')

plt.plot(x_1,y_1,label='stu_1')
plt.plot(x_2,y_2,label='stu_2')
plt.legend()
plt.show()