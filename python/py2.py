# ===============================================================关于复制的一些理解
#
a = 1
b = a
c = [1,2,3]
d = c
e = c.copy()    # c e 地址不同
print (a,b, id(a), id(b), c, d, id(c), id(d), e, id(e))
#  1 1 4407321952 4407321952 [1, 2, 3] [1, 2, 3] 4410784584 4410784584 [1, 2, 3] 4410784520
a = 2           # 此时a,b地址 不同  a != b
c[1] = 5        # 此时c,d地址 相同  c is d
print (a,b, id(a), id(b), c, d, id(c), id(d), e, id(e))
#  2 1 4407321984 4407321952 [1, 5, 3] [1, 5, 3] 4410784584 4410784584 [1, 2, 3] 4410784520

# ===============================================================函数
def fn1():
    print('hello')
fn1()                          # hello

def add(a, b):
    print (a, '+', b, '=', a+b)
add(1,1)                       # 1 + 1 = 2

def mul(a = 99, b = 2):        # 传递值 形参的默认值无作用 未传递值 形参有作用
    print (a*b)
mul()                            # 198
mul(3, b = 3)                   # 9
mul(a = 5)                      # 10
# 位置参数与关键字参数可以混合使用 必须将位置参数写在前面
# mul(fn1(),add(1,1))  #unsupported operand type(s) for *: 'function' and 'NoneType'

# 在函数中对形参进行重新赋值，不会影响其他的变量
# 如果形参执行的是一个对象，当我们通过形参去修改对象时  会影响到所有指向该对象的变量
def fun2(a):
    print (a, id(a))            #[1, 2, 3] 4385663816
    a[0] = 9
    print (a, id(a))            #[9, 2, 3] 4385663816
c = [1,2,3]
fun2(c)
print (c, id(c))                #[9, 2, 3] 4385663816

# 不定长的参数
# 在定义函数时，可以在形参前边加上一个*，这样这个形参将会获取到所有的实参 将会将所有的实参保存到一个元组中 只能有一个
# 可变参数不用写在最后，但是带*的参数后的所有参数，必须以关键字参数的形式传递
def fun3(*num):
    result = 0
    for i in num:
        result += i
    print (result)

fun3(1,2,3,4,5,6,7,8,9)         # 45

# *形参只能接收位置参数，而不能接收关键字参数
# **形参可以接收其他的关键字参数，它会将这些参数统一保存到一个字典中 字典的key就是参数的名字，字典的value就是参数的值 只能有一个 放在最后
def fun4(a, **key):
    print (a,key)

fun4 (1,name='xiaobai')         # 1 {'name': 'xiaobai'}

d = dict(name = 'jack', age = '18', number = '180')
def fun4(name, age, number):
    print(name, age, number)

fun4(*d)                        #name age number   获取的是可迭代对象的 key，所以函数的形参可以为位置参数或可变参数。 fun4()内形参可以与字典key不同
fun4(**d)                       # jack 18 180      获取的是可迭代对象的 value，所以函数的形参只能为关键字参数，即参数的个数和名称都是固定的。

# 如果仅仅写一个return 或者 不写return，则相当于return None
# 在函数中，return后的代码都不会执行，return 一旦执行函数自动结束  break 用来退出当前循环   continue 用来跳过当次循环

def fn5(a:int,b:bool,c:str='hello') -> int: #标准函数格式
    return 123

print (fn5(12,1,1))

# 作用域（scope）    全局变量 全局作用域     局部变量 局部作用域
# 函数内部修改全局变量，则需要使用global关键字，来声明变量
e = 11
def fn6():
    e = 33
    print (e)               # 33
    # global e
    # e = 66
    # print (e)             # 66
fn6()
print(e)                    #区分修改局部和全局变量的值

# locals()用来获取当前作用域的命名空间 返回字典
# globals() 函数可以用来在任意位置获取全局命名空间

e = 11
def fn7():
    e = 22
    # scope = locals()
    # print(scope)            #{'e': 22}
    scope_g = globals()
    print (scope_g)      #{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':............
    print (scope_g['e'])      # 11
    globals()['e'] = 33       # 全局变量的e ==> 33
fn7()
print(e)

# 高阶函数 接收函数作为参数，或者将函数作为返回值的函数为高阶函数
def func(i):
    return i > 10
# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中 参数：  1.根据该函数来过滤序列  2.序列       返回加list过滤后的新序列
# lambda语法： lambda 参数列表 : 返回值
# map()函数可以对可迭代对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回对应布尔值
def fn8(func, lst):
    n_list = []
    for i in lst:
        if func(i):
            n_list.append(i)
    return n_list


f = [1,2,3,5,6,76,5,78,456,7,634,26]

print (fn8(lambda i:i > 10, f))                     # [76, 78, 456, 634, 26]

print (list(filter(lambda i:i > 10, f)))            # [76, 78, 456, 634, 26]
print (list(map(lambda i:i > 10, f)))               # [False, False, False, False, False, True, False, True, True, False, True, True]

# sort()用来对列表中的元素进行排序 默认为大小 key = len  key = int
# sorted()可以对任意的序列进行排序 并且使用sorted()排序不会影响原来的对象 而是返回一个新对象
f.sort(key=int)
print (f)                                           #[1, 2, 3, 5, 5, 6, 7, 26, 76, 78, 456, 634]
g = [12,3,4,5,'6','7']
print (sorted(g,key = int))                         #[3, 4, 5, '6', '7', 12]
print (g)                                           #[12, 3, 4, 5, '6', '7']

# 闭包    通过闭包可以创建一些只有当前函数能访问的变量
# 形成闭包的要件 1 函数嵌套    2 将内部函数作为返回值返回  3 内部函数必须要使用到外部函数的变量
def make_average():
    nums = []
    def average(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return average

average = make_average()
# average是一个函数，是调用make_average()后返回的函数
# 此函数在fn()内部定义，并不是全局函数 总是能访问到fn()函数内的变量

for i in range(0, 100, 10):
    print (average(i))                              #0.0 5.0 10.0 15.0 20.0 25.0 30.0 35.0 40.0 45.0

# 装饰器
# 开闭原则（OCP） 开发对程序的扩展，要关闭对程序的修改
# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，来装饰当前的函数

def zs(old):
    def new_function(*args, **kwargs):
        print ('begin')
        result = old(*args, **kwargs)
        print ('end')
        return result
    return new_function

def zs1(old):
    def new_function(*args, **kwargs):
        print ('hello')
        result = old(*args, **kwargs)
        print ('bye!!!')
        return result
    return new_function

# @zs
# fun_zs = zs(make_average)
# average = fun_zs()    # 此时只输出输出 begin end

average_1 = make_average()
average = zs(average_1)
# 此时同样 当调用average()时 在return的时候只是ruturn   average_1() 没有真实输出

for i in range(0, 100, 10):
    print (average(i))

@zs1
def say_hello():
    print('大家好~~~')
say_hello()
