# #========================================================================变量
# 直接使用变量赋值 不可以使用无赋值的变量 动态语言 可以任意变更赋值类型或值
# 数值分成了三种：整数(int)、浮点数(float)(不精确)、复数   没有大小限制
a = 999999 ** 100
# print (a)

# 字符串 (单/双)引号括起来 相同引号不能嵌套    用 \ 来换行输出
# 三重引号来表示一个长字符串 ''' """ 中间可以换行
b = '''hello
nihao'''
print (b)                # hello    \    nihao

# 转义字符： \t 表示制表符 \n 表示换行符 \\ 表示反斜杠  \u 表示Unicode编码  \" 表示"
c = '\u6668'
print (c)                # 晨

#  占位符  %s 在字符串中表示任意字符  %f 浮点数占位符   %d 整数占位符
#  %3.5s字符串的长度限制在3-5之间      %.2f 保留后两位小数
d = 'hello %s'%'jack1'
print (d)                # hello jack1
d = 'hello %s nihao %s'%('jack2','rose')
print (d)                # hello jack2 nihao rose
e = 'nice %.2f and %2f and %d'%(12.34567, 9876.5432, 1.98) # %d只保留整数位
print (e)                # nice 12.35 and 9876.543200 and 1

#   格式化字符串，字符串前添加一个f来创建一个格式化字符串
f = f'!!!add {c}'
print(f)                # !!!add 晨

#   字符串运算，两个字符串进行相加，则两个字符串拼接为一个
g = c + f
print (g)                # 晨!!!add 晨

#   字符串的复制  将字符串和数字相乘 将字符串重复指定的次数并返回
h = '*' * 50
print (h)                # **************************************************

#   布尔值     两个 True 和 False       None用来表示不存在
print (None)                # None

#   类型查验 type()用来检查值的类型 将检查的结果作为返回值   可用变量来接收返回值
print (type(1))              # <class 'int'>
print (type(1.2))            # <class 'float'>
print (type(True))           # <class 'bool'>
print (type('nice'))         # <class 'str'>
print (type(None))           # <class 'NoneType'>

#   类型转换    str() 可以将对象转换为字符串    bool() 可以将对象转换为布尔值 ===》 0 None '' 转False
#   int() 可以用来将其他的对象转换为整型
#       布尔值：True -> 1   False -> 0
#       浮点数：直接取整，省略小数点后的内容
#       字符串：合法的整数字符串，直接转换为对应的数字。 不合法 抛出错误
#   float() 和 int()类似 ，它会将对象转换为浮点数

#   算术运算符
#       + 加法（如果是两个字符串之间进行加法运算，则会进行拼串操作）
#       - 减法
#       * 乘法（如果将字符串和数字相乘，则会对字符串进行复制操作，将字符串重复指定次数）
#       / 除法，结果返回一个浮点型
#       // 整除，只会保留计算后的整数位，返回一个整型
#       ** 幂运算，求一个值的几次幂
#       % 取余数

#   赋值运算符
#       +=  -=   *=  /=   //=    **=    %=

#   关系运算符 返回布尔值
#       >   >=   <   <=   ==    !=     is     is not (is & is not  比较对象id)
#       is & is not  比较对象id(内存地址)         字符串比较Unicode编码  可强转int比较
print (id(0), id(False))        # 4557833536 4557454176

#   逻辑运算 布尔值进行比较
#   not     and     or

#   条件运算符   语句1 if 条件表达式 else 语句2   判断结果为True，执行语句1，返回结果 否则执行语句2
max_if = 100 if 100 > 99 else 99
print (max_if)                     # 100

#   运算符优先级
print (10 < 50 > 30)            # True
#   等同于 10 < 50 and 50 > 30
print (1 or 2 and 3)            # 1
#   and > or     2 and 3 ==> 3      1 or 3 ==> 1


# #========================================================================输入输出
# print中 用 \ 来换行输出
print ('ni\
hao')

# input
# location = input('input=')
#  自上而下执行

# #========================================================================流程控制
#   if判断
if True : print('*'*50)
if 9 > 10:
    print(999999)
    print(888888)

#   if elif else
i = 100
if i > 300:
    print ('i > 300')
elif i > 200:
    print ('200 < i <= 300')
else:
    print ('i < 200')

#   while循环
# while condition:
#     # code
# else:
#     # code
# break可以用来立即退出循环语句（包括else）
# continue可以用来跳过当次循环  和break一样 只是对最近对循环起作用
i = 0
while True:
    print (i)
    i += 1
    if i > 6:
        break

#     for循环
for j in range(10):
    print(j)

# #========================================================================列表
#   列表中可以存储多个元素，可在创建列表时指定列表中的元素
k = [1, 'nihao', True, None, print]
l = ['nihao', 'jack', 'rose', 'tom', 'jerry', 1]
print (k)                   # [1, 'nihao', True, None, <built-in function print>]
print (k[3])                # None
print (k[1:])               # ['nihao', True, None, <built-in function print>]
print (k[:4])               # [1, 'nihao', True, None]

#   语法：列表[起始:结束:步长]  步长默认为1 如果是负数，则会从列表的后部向前边取元素
print (k[::2])              # [1, True, <built-in function print>]
print (k[::-1])             # [<built-in function print>, None, True, 'nihao', 1]

#   +可以将两个列表拼接为一个列表     * 可以将列表重复指定的次数
print (k[::2] + l[1:3])     #[1, True, <built-in function print>, 'jack', 'rose']
print (l[1] * 3)            #jackjackjack

# in 和 not in   用来检查指定元素是否存在于列表中
# len()获取列表中的元素的个数
# min() 获取列表中的最小值
# max() 获取列表中的最大值
print ('nihao' in l)
print (len(k))              # 5
m = [1,23,4,5,67,86,754,23,45,2]
print (max(m))              # 754
print (min(m))              # 1
# 两个方法
# index() 获取指定元素在列表中的第一次出现时索引 第二个参数，表示查找的起始位置,第三个参数,表示查找的结束位置
# count() 统计指定元素在列表中出现的次数
print (l.index('tom'))      # 3
print (l.count('tom'))      # 1

# l = ['nihao', 'jack', 'rose', 'tom', 'jerry', 1]
# 通过del来删除元素
# 通过 list() 函数将其他的序列转换为list
l[4:] = ['jackson', 2]
print(l)                    #['nihao', 'jack', 'rose', 'tom', 'jackson', 2]
del l[5]
print(l)                    #['nihao', 'jack', 'rose', 'tom', 'jackson']
n = 'nice'
n = list(n)
print(n)                    #['n', 'i', 'c', 'e']

# 列表的方法
# append() 向列表的最后添加一个元素
# insert() 向列表的指定位置插入一个元素   参数1 位置 参数2 元素
# extend() 使用新的序列来扩展当前序列
# pop()    根据索引删除并返回被删除的元素 参数: 索引 若不写参数 删除最后一个
# remove() 删除指定值得元素，如果相同值得元素有多个，只会删除第一个
# reverse()用来反转列表
# sort()   用来对列表中的元素进行排序，默认是升序排列 如果需要降序排列，传递一个reverse=True作为参数
# clear()   清空序列
#m = [1,23,4,5,67,86,754,23,45,2]
print(m)                    #[1, 23, 4, 5, 67, 86, 754, 23, 45, 2]
m.append(3)
print (m)                   #[1, 23, 4, 5, 67, 86, 754, 23, 45, 2, 3]
m.insert(0, 0)
print (m)                   #[0, 1, 23, 4, 5, 67, 86, 754, 23, 45, 2, 3]
m.extend([9,8,7])
print (m)                   #[0, 1, 23, 4, 5, 67, 86, 754, 23, 45, 2, 3, 9, 8, 7]
m_pop = m.pop(0)
print (m_pop)               #0
m.remove(3)
print (m)                   #[1, 23, 4, 5, 67, 86, 754, 23, 45, 2, 9, 8, 7]
m.reverse()
print (m)                   #[7, 8, 9, 2, 45, 23, 754, 86, 67, 5, 4, 23, 1]
m.sort()
print (m)                   #[1, 2, 4, 5, 7, 8, 9, 23, 23, 45, 67, 86, 754]
m.clear()
print (m)                   #[]

# 通过for循环来遍历列表
for i in l:
    print (i)               # nihao jack rose tom jackson

# #========================================================================复制
# copy() 方法用于对对象进行浅复制 与原对象独立 简单复制对象内部的值 如果值也是一个可变对象 不会被复制
q1 = [10,20,30]
print (q1, id(q1))          # [10, 20, 30] 4507701192
q2 = q1             # q1 q2 id相等 q2改变 q1也改变
q3 = q1.copy()
q2[2] = 100
print (q1, id(q1))          # [10, 20, 100] 4507701192
print (q2, id(q2))          # [10, 20, 100] 4507701192
print (q3, id(q3))          # [10, 20, 30] 4508057864

# #========================================================================元祖 tuple
# 元祖是不可变的序列 不可以赋值
p = (10,20,30,40,50)  # 当元组不是空元组时，括号可以省略
# 解包指是将元组当中每一个元素都赋值给一个变量
# 可以在变量前边添加一个*，变量会获取元组中所有剩余的元素 不允许同时出现两个或以上的*变量
a1, a2, a3, a4, a5 = p
b1, *b2, b3 = p
print(a1, a2, a3, a4, a5)   # 10 20 30 40 50
print (b1)                  # 10
print (b2)                  # [20, 30, 40]
print (b3)                  # 50

# #========================================================================字典
#  字典的值可以是任意对象 字典的键可以是任意的不可变对象 一般使用str字典的键不能重复 出现重复时后边会替换到前边
#  {key:value,key:value,key:value}
r = {'name' : 'rose',
    'age' : 22,
    'gender' : 'girl'
    }

# 根据键来获取值
print (r['name'], r['gender'])   # rose girl

# 使用 dict()函数来创建字典 2种方法
s = dict([('name' , 'libai'), ('age' , 24), ('gender' , 'man')])
s = dict(name = 'libai', age = 24, gender = 'man')

# in 检查字典中是否包含指定的键      not in 检查字典中是否不包含指定的键
print ('name' in s)             #True

# len() 获取字典中键值对的个数
# get(key[, default]) 用来根据键来获取字典中的值  指定一个默认值，来作为第二个参数，这样获取不到值时将会返回默认值
# setdefault(key[, default]) 可以用来向字典中添加key-value   若key存在 返回key值 不存在添加key值并设置value值
# update([other])   将其他字典中的key-value添加到当前字典中   如果有重复的key，则后边的会替换到当前的
# 使用 del 来删除字典中的 key-value
# popitem()  随机删除字典中的一个键值对 一般删除最后一个键值对 返回值返回删除的key-value
# pop(key[, default]) 根据key删除字典中的key-value 指定一个默认值，来作为第二个参数 再删除不存在的key时，不会报错，而是直接返回默认值 返回值返回删除的value
# clear()用来清空字典
print (len(s))                  # 3
print (s['name'])               #libai
print (s.get('name'))           #libai
s['name'] = 'xiaobai'
print (s)                       # {'name': 'xiaobai', 'age': 24, 'gender': 'man'}
print (s.setdefault('age',20))  # 24
s.update({'loc' : 'shanghai'})
print (s)                       # {'name': 'xiaobai', 'age': 24, 'gender': 'man', 'loc': 'shanghai'}
del s['loc']
print (s)                       #{'name': 'xiaobai', 'age': 24, 'gender': 'man'}
print (s.popitem())             # ('gender', 'man')
print (s)                       # {'name': 'xiaobai', 'age': 24}
print (s.pop('age'))            # 24
print (s)                       # {'name': 'xiaobai'}
s.clear()
print (s)                       # {}

# 三种遍历字典的方法
# keys() 该方法会返回字典的所有的key
for i in r.keys():
    print (i, ' ', r[i])  # name   rose  \ age   22  \  gender   girl
# values() 该方法会返回一个序列，序列中保存有字典的左右的值
for i in r.values():
    print (i)             # rose  \  22   \   girl
# items() 该方法会返回字典中所有的项  它会返回一个序列，序列中包含有key values
for i,j in r.items():
    print (i, ' ', j)     # name   rose  \ age   22   \  gender   girl

# #========================================================================集合
# 使用 {} 来创建集合  不能有列表   是一个无序不重复元素集  set不记录元素位置或者插入点
# set() 将序列和字典转换为集合 将字典转换为集合时只包含字典中的键
# r = {'name' : 'rose','age' : 22,'gender' : 'girl'}
t = set (r)
print (t)                 # {'name', 'gender', 'age'}
u = {1, 2, 3, 'a', 'b'}
print (u)                 # {1, 2, 3, 'a', 'b'}

# 使用in和not in来检查集合中的元素
print ('name' in t)       # True

# 使用len()来获取集合中元素的数量
print (len(t))            # 3

# add() 向集合中添加元素
t.add('loc')
print (t)                 # {'loc', 'gender', 'age', 'name'}

# update() 将一个集合中的元素添加到当前集合中 可以传递序列或字典作为参数 字典只会使用键
t.update(set('nice'))
print (t)                 # {'gender', 'loc', 'c', 'age', 'i', 'name', 'n', 'e'}
t.update(set(dict(number = 180)))
print (t)                 # {'gender', 'loc', 'c', 'age', 'i', 'name', 'n', 'number', 'e'}

# pop()随机删除并返回一个集合中的元素
print (t.pop())           # n
print (t)                 # {'name', 'c', 'age', 'e', 'i', 'number', 'gender', 'loc'}

# remove()删除集合中的指定元素
t.remove('c')
print (t)                 # {'gender', 'n', 'name', 'number', 'e', 'i', 'loc'}

# clear()清空集合
t.clear()
print (t)                 # set()

# copy()对集合进行浅复制
v = u.copy()
print (u)                 # {1, 2, 3, 'a', 'b'}

w = {2, 3, 4, 'a', 'c'}

# & 交集运算    | 并集运算       - 差集        ^ 异或集       <= 一个集合是否是另一个集合的子集
# < 检查一个集合是否是另一个集合的真子集    >= 超集     > 真超集
print (u & w)             #{2, 3, 'a'}
print (u | w)             #{1, 2, 3, 4, 'a', 'b', 'c'}
print (u - w)             #{1, 'b'}
print (u ^ w)             #{1, 4, 'b', 'c'}
print (u <= v)            #True
print (u < v)             #False
