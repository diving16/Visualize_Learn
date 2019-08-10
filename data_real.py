from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data1 = pd.read_csv('11-17_allresult.csv')

#改变输出显示为不限制
pd.set_option('display.max_rows', 10) 
pd.set_option('display.max_columns', 4) 

#找出指定数据
Build_MengMinwei_filter = data1.F_BuildName == '蒙民伟楼'
data_Build_MengMinwei = data1[Build_MengMinwei_filter]

#修改index
data_Build_MengMinwei.index= range(1,len(data_Build_MengMinwei)+1)
num_F_MeterID = len(set(data_Build_MengMinwei.F_MeterID))

#利用生成器对大数据切片
#def chunker(iterable,size,start=0):
#    for i in range(start,len(iterable),size):
#        yield iterable[i:i+size]


#terminal_chunks = list(chunker(data_Build_MengMinwei,
#                         int(len(data_Build_MengMinwei)/num_F_MeterID),
#                         0))

#print(terminal_chunks)

#经过尝试，在for循环里操作list或者Dataframe总是结果没有该表，drop不掉。
#terminal_24h=[]

#for terminal_chunk in terminal_chunks:
#    terminal_chunk.index= range(1,len(terminal_chunk)+1)
#    terminal_24h.append(terminal_chunk)
  
#print(terminal_24h)

#直接通过对数据的了解删除指定位置的数据
drop_index_filter=data_Build_MengMinwei.index % 169 == 0
data_Build_MengMinwei.drop(data_Build_MengMinwei[drop_index_filter].index,inplace=True)

#print(data_Build_MengMinwei)
#print(len(data_Build_MengMinwei))

#利用生成器对大数据切片
def chunker(iterable,size,start=0):
    for i in range(start,len(iterable),size):
        yield iterable[i:i+size]


terminal_chunks = list(chunker(data_Build_MengMinwei,
                         int(len(data_Build_MengMinwei)/num_F_MeterID),
                         0))

#print(terminal_chunks)

#对每个分块修改index
for terminal_chunk in terminal_chunks:
    terminal_chunk.index = range(1,len(terminal_chunk)+1)


