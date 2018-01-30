#2018/1/30
"""
str.capitalize()
Return a copy of the string with its first character capitalized and the rest lowercased.

利用capitalize()可以实现：
把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
下面是几个实现
"""
def normalize(name):
    return name.capitalize()

def normalize1(name):
    for x in range(len(name)):
        if x==0:
            name=name[:x]+name[x].upper()+name[x+1:]
        else:
            name=name[:x]+name[x].lower()+name[x+1:]
    return name
 
def normalize2(name):
    t=''
    for x in range(len(name)):
        if x==0:
            t=name[0].upper()
        else:  
            t=t+name[x].lower()
    return t
#test 
L1 = ['adam', 'LISA', 'barT','',' aa']
L2 = list(map(normalize, L1))
L3 = list(map(normalize1, L1))
L4 = list(map(normalize2, L1))
print(L2)
print(L3)
print(L4)
"""
运行结果：
['Adam', 'Lisa', 'Bart', '', ' aa']
['Adam', 'Lisa', 'Bart', '', ' aa']
['Adam', 'Lisa', 'Bart', '', ' aa']
"""
 
