#变量学习
# type()可以查看变量类型
# id()可以查看变量内存地址
# 变量的创建不需要声明

#变量的基本类型有：
#数字(num):int long float complex bool
#字符串(str)
# 高级数据类型
#元组(tuple)
#字典(dict)
#列表(list)
a = 10
print(type(a))
print(a)
a= 20
print(a)
a= 'abcdefg'
print(a)
print(id(a))
################################################################
b = ()  #元组类型
print(type(b))
c = {}  #字典类型
print(type(c))
d = []  #列表类型
print(type(d))
################################################################
# 变量命名规则
# 跟C语言一样
print(a,b,c)
_age = 90
print(_age, a)