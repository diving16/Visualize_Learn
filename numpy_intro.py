import numpy as np

#[1 2 3 4]
#[5 6 7 8]
#[9 10 11 12]

#shape(3,4)

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(a)

b=a[:2,1:3]
b[0,0]=8888

print(b)

#注意：b变化时，a也会变化
print(a)

#快速生成array的方法
c=np.zeros((2,20))
print(c)

d=np.ones((20,5))
print(d)

e=np.full((5,7),233)
print(e)

f=np.eye(10)*20
print(f)

g=np.random.random((3,4))
print(g)

#用index取消array的关联
h=np.array([[1,2],[3,4],[5,6]])
# =============================================================================
# print(h)
# i=np.array([h[0,1],h[1,1],h[2,0]])
# print(i)
# i[[0,0]]=233
# print(i)
# print(h)
# =============================================================================
i=h[[0,1,2],[0,1,0]]
print(i)

j=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(j)
k=np.array([0,2,0,1])
print(k)

j[np.arange(4),k]+=100
print(j)
#np.arange(4)给出每行，k是每行取出来的序号

l=j[np.arange(4),k]
print(l)
print(np.arange(4))

m=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)

#布尔值贴标签
boolean_array_indexing = (m>5)
print(boolean_array_indexing)
print(m[m>4])

#array的加法
x=np.array([[1,2],[3,4]],dtype=np.float64)
print(x)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print(y)

print(x+y)
print(np.add(x,y))

#四则运算,开方
print(x-y)
print(np.subtract(x,y))

#每个元素逐一对应相乘
print(x*y)
print(np.multiply(x,y))

print(x/y)
print(np.divide(x,y))

print(np.sqrt(x))

#numpy dot 点乘
print(x.dot(y))
print(np.dot(x,y))

x1=np.array([3,0])
y1=np.array([0,4])
print(np.dot(x1,y1))


#小技巧
#求和运算
x2=np.array([[1,2],[3,4],[5,6]])
print(x2)
print(np.sum(x2))
#axis=0是按列，axis=1是按行
print(np.sum(x2,axis=0))
print(np.sum(x2,axis=1))

#转置
print(x2.T)

#broadcast，类似于脑补,相当于y2=np.array([[0,1],[0,1],[0,1]])
x3=np.array([[1,2,3],[3,4,5],[5,6,8],[7,8,9]])
print(x3)
print(x3[1,:2])
print(x3[1,:])
y3=np.array([1,0,1])

print(y3)
print(x3+y3)

#numpy.empty_like的用法,随机生成的内容
#np.ones_like(x),np,zeros_like(x)
z1=np.empty_like(x3)
print(z1)

#broadcast原理解释
for i in range(4):
    z1[i,:]=x3[i,:]+y3
    
print(z1)



