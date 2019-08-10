import numpy as np

#观察会发现和list不同的是，print后没有逗号
#numpy的array内容不能变，内容类型一样的，可以数学运算，这些区别于list
V=np.array([1,2,3,4,5,6,7,8,9,10])

M=np.array([[1,2,3,4,5,6,7,8,9,10],
           [10,9,8,7,6,5,4,3,2,1]])

#修改数据类型,float,complex,bool
M_1=np.array([[1,2,3,4,5,6,7,8,9,10],
           [10,9,8,7,6,5,4,3,2,1]],dtype=float)

M_2=np.array([[1,2,3,4,5,6,7,8,9,10],
           [10,9,8,7,6,5,4,3,2,1]],dtype=complex)

M_3=np.array([[0,2,3,4,5,6,7,8,9,10],
           [10,9,8,7,6,5,4,3,2,1]],dtype=bool)


print(type(V))
print(M)
print(M_1)
print(M_2)
print(M_3)

print(M.shape)
print(np.shape(M))
print(np.size(M))

print(M.dtype)

#ndarray只有同一数据类型才能替换
#M[0,0]='Hello'
M[0,0]=2
print(M)

