# num = 1
# list1 = [1,2,3,4]
# print(tuple(list1))
# 三目运算符 表达式 if 条件 else 条件不符合执行的表达式
# a = 1
# b = 2 
# c = a if a > b else b 
# print(c) 
# i = 0
# while i <= 5:
#     if i == 3:
#         print('sorry')
#         i += 1
#         continue
#     print("Happy")
#     i += 1
# print("Nice")
# f = 'hello '\
#     'world'
# print(type(f))

# 切片操作
# name = 'jeromecloud'
# print(name[3:6:3])
# 序列【开始位置下标：结束位置下标：步长】，
# 步长默认为1。选取方向为从左到右，步长为负数，选取方向为从右到左
# 步长方向和数据选取方向要一致
# 不包括开始和结束位置的数据
# 不写开始和结束的话代表选择所有
# 选择负数的话可以倒序排列
# -1代表最后一个数据
# print(name[::-1])

# mystr = "hello world jeromecloud"
# print(mystr.find('world',1,11)) 
# find(查找内容（子字符串），开始位置，结束位置)，若存在返回字符串起始位置，不存在返回-1
# 开始和结束位置可省略
# mystr.index()
# print(mystr.replace('hello','fuck'))
# print(mystr.split(' ',3))   split分割字符串，返回列表
# join(合并序列)
# ljust(10,'')左对齐，10个长度，填充字符

# 将8个老师随机分配到3个办公室
# import random
# teacher = ['A','B','C','D','E','F','G','H']
# offices = [[],[],[]]
# for name in teacher:
#     num = random.randint(0,2)
#     offices[num].append(name)
# # print(offices)
# for office in offices:
#     # print(office)
#     print(f"办公室人数是{len(office)},人数分别是{office}")

# tuple
# t1 = ('10','222','33333')
# print(t1)
# print(type(t1))
# t2 = (10)
# print(type(t2))

# dict
# dict1 = {
    # 'name':'Tom',
    # 'gender':'男'
# }
# dict1['age'] = '111'
# print(dict1)
# print(type(dict1))
# print(dict1['name']) #通过键来查找值
# print(dict1.get('sss','?')) #通过get来查找，如果没有返回第二个值，如果没有第二个值则none
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# for key in dict1.keys():
    # print(key)
# for value in dict1.values():
    # print(value)
# for key,values in dict1.items():
    # print(f"{key} = {values}")
# for item in dict1.items():
    # print(item)

# set {}或set(),集合，没有重复数据，没有顺序，不支持下标
# set1 = {10,20,30,40}
# print(set1)
# print(type(set1))
# set2 = set('asdfghsdaf')#此种方式至多创建一个参数
# print(set2)
# set3 = {'jerome','hahha'}
# set3.add('cloud')# 此方式只可追加集合中不存在数据，不可追加序列
# print(set3)
# set4 = {12,234,5463,342}
# set4.update([999,9999,999999])# 此方式只可追加序列
# print(set4)

# hello = 'hello world'
# print('jj' not in hello) #返回True

# 公共运算符
""" str1 = 'hello'
str2 = 'world'

list1 = ['jeromecloud','cloud']
list2 = ['meet','beautiful']

tuple1 = (999,888,777)
tuple2 = (666,555,444)

dict1 = {
    'name' : 'Tony',
    'age'  :  99,
}
dict2 = {
    'gender':'男',
    'phone' :13815846933,
}

set1 = {10,20,30}
set2 = {111,222,333}
 """
# +合并运算，支持str,list,tuple
# print(str1 + str2)
# print(list1 + list2)
# print(tuple1 + tuple2)
# * 运算，支持str,list,tuple
# print(str1 * 5)
# print(list1 * 5)
# print(tuple1 * 5)

# range函数,不包括结束位置数据
# for i in range(1,10,1):
    # print(i)

# enumerate(可遍历对象，start=0) 枚举函数，start=0:遍历下标起始值，默认为0
# list1 = [10,20,30,40,50,60,70,80,90]
# for i in list1:
#     print(i)
""" 
10
20
30
40
50 
"""
# for i in enumerate(list1):
#     print(i)
""" 
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, 50) 
"""

# 列表推导式
# list1 = []
# i = 0 
# while i <10 :
#     list1.append(i)
#     i += 1
# print(list1)

# list1 = []
# for i in range(10):
#     list1.append(i)
#     i += 1
# print(list1)

# list1 = [i for i in range(10)] # i 是返回值
# print(list1)

# list1 = ['name','age','gender']
# list2 = ['jerome','22','man']
# dict1 = {i:j for i in list1 for j in list2} 
# 写法1
# dict1 = {list1[i]:list2[i] for i in range(len(list1))}
# 写法2
# print(dict1)

# 获取字典中的数据
# counts1 = {
    # 'Macbook': 300,
    # 'Dell': 234,
    # 'HP': 12,
    # 'Lenovo': 2,
    # }
# data = {key:value for key,value in counts1.items() if value > 200}
# print(data)

# 函数
# def count1(a,b):
    # """ 简单计算 """
    # return a + b 
# print(count1(10,20))
# 查看函数说明文档 help(函数)

# a = 100
# def testA():
    # global a
    # a = 300
    # print(a)
# testA()
# print(a)
""" 
300
300
"""

# 多个返回值
# def test2():
    # return 1,2  # 返回一个元组
    # return [1,2,3]  # 返回列表
    # return {'a':1,'b':2} # 返回字典
# print(test2())

# 位置参数，个数和顺序必须保持一致
# def test3(name,age,gender):
#     print(f" {name} is nice, your {age} is bad, you is a {gender} guy")
# test3('jerome',22,'man')

# 关键字参数，不需要顺序一致，如果有位置参数，必须在关键字参数前面，缺省参数放在最后
# def test3(name,age,gender='woman'):
#     print(f" {age} is nice, your {name} is bad, you is a {gender} guy")
# test3(name='jerome',age=22)
    
# 不定长参数，包裹位置传递，接受位置参数，返回一个元组    
# def test4(*args):
#     print(args)
#     return args
# test4('hello','world')
# a, b = test4('hello','Mac') # 拆包
# print()
# # 包裹关键字传递
# def test5(**kwargs):
#     print(kwargs)
#     return kwargs
# test5(name='jerome',age=11)
# result = test5(name='Tony',gender='man')
# a, b =result    # 字典解包,对字典解包首先取出的key值
# print(a)
# print(b)
# print(result[a])
# print(result[b])

# a = 'Jerome'
# b = 'Tmall'
# a, b = b, a 
# print(a)
# print(b)

# int 不可变类型
# a = 3
# b = a 
# print(id(a))
# print(id(b))
# b = 4
# print(id(b))
"""
4408175856
4408175856
4408175888 
"""
# 列表 可变类型
# aa = ['jerome','cloud']
# bb = aa
# print(id(aa))
# print(id(bb))
# aa.append('Tony')
# print(id(bb))
# print(id(aa))
""" 
4401799048
4401799048
4401799048
4401799048
"""

# 可变类型：列表、字典、集合
# 不可变类型：整型、浮点型、元组、字符串

# lambda（匿名函数）:如果函数只有一个返回值，并且只有一句代码
# 格式： lambda 参数a，参数b，…… ：表达式
# lambda参数可有可无，能接受任意参数，但只能返回一个值
# 直接输出f1，为lambda的内存地址，加括号则为函数输出
# def f1():
#     return 100
# print(f1())
# f2 = lambda: 100+200
# print(f2())
# f3 = lambda a, b: a + b
# print(f3(4,5))
# 缺省参数
# f4 = lambda *args: args
# print(f4(100,200))
""" 
（100，200）
"""
# 可变参数
# f5 = lambda **kargs: kargs
# print(f5(name='python', age=20))
"""
 {'name': 'python', 'age': 20}
"""
# 带判断的lambda
# f6 = lambda a, b: a if a > b else b
# print(f6(111,222))
# 排序
# students = [
#     {'name': 'Jerome', 'age': 20},
#     {'name': 'Cloud', 'age': 30},
#     {'name': 'Robert', 'age': 15}
# ]
# #按name值进行升序
# students.sort(key= lambda x: x['age'])
# print(students)
# #按name值进行降序
# students.sort(key= lambda x: x['age'], reverse=True)
# print(students)

#高阶函数
# def add_num(a,b):
    # return abs(a) + abs(b)
# result = add_num(3, -3)
# print(result)
#进阶
# def add(a,b,f):
    # return f(a) + f(b)
# result = add(3,-2,abs) # 将函数作为参数传入
# print(result)
