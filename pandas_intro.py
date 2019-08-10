import pandas as pd

#dataframe
#每一列是一个series

pd.set_option('display.max_row',100)
pd.set_option('display.max_columns',100)

#批量输入及更改header
#user_input_cols=['a1','a2','a3',
#                 'a4','a5','a6',
#                 'a7','a8','a9']

df=pd.read_csv('diabetes.csv',)
#               names=user_input_cols)
#header的意义：如果第一行不是header，可以如下操作：
#df=pd.read_csv('diabetes.csv',header=None)
#查看pandas.read_csv文档，关注delimiter,index_col(指定某一列为index)
#df=pd.read_csv('diabetes.csv',index_col=0)

print(df.head())

# =============================================================================
# #读取某一列，这个方法比df.a2适用更广
# print(df['a1'].head())
# 
# print(type(df['a1']))
# 
# print(df.a2.head())
# 
# print(df.shape)
# 
# #series相加,是一个拼起来的series，加上一个逗号会好看
# new_series=df['a1']+','+df['a2']
# print(type(new_series))
# #把series放回dataframe,对dataframe进行变更
# df['s+s']=new_series
# print(df.head())
# 
# 
# =============================================================================
#为什么有的有括号，有的没括号，比如df.dtypes是一种特性，
#df.head()相当于对对象进行操作，一种方法，空括号是因为没有参数传入。
#举例：df.shape也是一种特性。

#拿到数据之后的总体描述
#对于非数值型数据，会产生另一种统计，count,unique,top,freq
print(df.describe())

