import matplotlib.pyplot as plt
import numpy as np

x,y=np.loadtxt('E:/python_wangyi/visualize_learn/example_csv.txt',
               delimiter=',',
               unpack=True)

plt.plot(x,y,label='load data')
plt.legend()

plt.xlabel('x')
plt.ylabel('y')
plt.title('load a file')

plt.show()
