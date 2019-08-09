import matplotlib.pyplot as plt

City_A_Age=[1,2,5,7,8,4,6,7,9,10,13,8,14,15,18,19,20,21,25,24,
            28,29,24,27,30,36,34,37,39,40,46,48,47,50,54,58,
            1,3,45,7,2,5,8,7,9,68,4,7,34,8,28,87,3,24,16,15,78,
            60,67,64,70,89,60,90,100,8,14,15,18,19,2]

bins=[0,10,20,30,40,50,60,70,80,90,100,110]

plt.hist(City_A_Age,bins,histtype='bar',rwidth=0.8)



plt.xlabel('Age')
plt.ylabel('Num')
plt.title('The city age hist')
plt.legend()

plt.show()