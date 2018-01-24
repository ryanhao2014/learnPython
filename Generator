### practice杨辉三角 generator实现及遇到的问题
#### 实现1
`
def triangles():
    b=[1]
    while True:
        yield b
        for i in range(len(b)-1):
           b[i]=b[i]+b[i+1]
        b.insert(0,1)
n1=0
s1=[]
for t in triangles():
    print(t)
    s1.append(t)
    n1=n1+1
    if n1==3:
        break`
        
        
        
        
        
#### 实现2        
`
def triangles2():
    b=[1]
    while True:
        yield b
        b= [1]+[b[i] + b[i+1] for i in range(len(b)-1)]+[1]
n2=0
s2=[]
for t2 in triangles2():
    print(t2)
    s2.append(t2)
    n2=n2+1
    if n2==3:
        break`
     
    发现s1 s2并不相同
    作对比为：
    `
    n1=0
s1=[]
for t in triangles():
    print(t,type(t),'      s1= ',s1)
    s1.append(t)
    print(s1)
    a=t
    n1=n1+1
    if n1==3:
        break
print('------------------------------------------------------------------')
n2=0
s2=[]
for t2 in triangles2():
    print(t2,type(t2),'      s2=',s2)
    s2.append(t2)
    print(s2)
    c=t2
    n2=n2+1
    if n2==3:
        break
if a==c:
    print('a==c')
    if s1==s2:
        print('s1==s2')
    else:
            print('what??????')
            `
            运行结果为
 >           
[1] <class 'list'>       s1=  []
[[1]]
[1, 1] <class 'list'>       s1=  [[1, 1]]
[[1, 1], [1, 1]]
[1, 2, 1] <class 'list'>       s1=  [[1, 2, 1], [1, 2, 1]]
[[1, 2, 1], [1, 2, 1], [1, 2, 1]]
------------------------------------------------------------------
[1] <class 'list'>       s2= []
[[1]]
[1, 1] <class 'list'>       s2= [[1]]
[[1], [1, 1]]
[1, 2, 1] <class 'list'>       s2= [[1], [1, 1]]
[[1], [1, 1], [1, 2, 1]]
a==c
what??????

即s1在调用append()之后出现了与s2不同的结果
尚未发现其原因
