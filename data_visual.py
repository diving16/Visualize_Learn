from matplotlib import pyplot as plt
import pandas as pd

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,3,5,6,7,8,9,10,13,17]
z=[2,4,6,8,10,11,12,14,16,20]

plt.plot(x,y,'x')
plt.plot(x,z,'o')
plt.legend(['y legend','z legend'])

plt.xlabel('x')
plt.ylabel('y and z')
plt.title('Two plots')

plt.show()


