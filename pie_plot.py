import matplotlib.pyplot as plt

sales=[1.8,2,3.5,7.8]
company_names=['A','B','C','D']
colors_1=['azure','lavender','pink','grey']

plt.pie(sales,
        labels=company_names,
        colors=colors_1,
        startangle=90,
        shadow=True,
        autopct='%1.2f%%',
        explode=(0.1,0,0,0))

plt.legend()
plt.show()
