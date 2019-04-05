# =======================================类
# 在类的代码块中，可以定义变量和函数 会成为所有的实例的公共属性 所有实例都可以访问这些变量
# isinstance()用来检查一个对象是否是一个类的实例
# 方法每次被调用时，解析器都会自动传递第一个实参self 就是调用方法的对象本身 在方法中不能直接访问类中的属性
class Peopel:
    name = 'xiaobai'
    def fun1(self):
        print('hello, this is :', self.name)
p1 = Peopel()
p2 = Peopel()
print (isinstance(p1,Peopel))               #Ture

# 通过对象来修改属性
p2.name = 'jack'
p2.fun1()                                   #hello, this is : jack
p1.fun1()                                   #hello, this is : xiaobai
# del p2.name # 删除p2的name属性

# 在类中可以定义一些特殊方法（魔术方法） 以__开头，__结尾  不需要人为调用  在特殊时刻自动调用
    #   1.创建一个变量
    #   2.在内存中创建一个新对象
    #   3.__init__(self)方法执行
    #   4.将对象的id赋值给变量
class Person:
    def __init__(self, name):
        self.name = name        # 通过self来调用
    def fun(self):
        print ('hello', self.name)

p3 = Person('rose')
p3.fun()                                    # hello rose
print(p3.name)

# 对象中具有一个特殊方法__len__, 以通过len()来获取它的长度
print(len('nice'))                      #4

# =======================================================封装
# 隐藏对象中一些不希望被外部所访问到的属性或方法     用getter和setter方法
# 增加了复杂度 但保证数据安全性 只读：去掉setter 不能被访问：去掉getter
# 使用setter方法设置属性，可以增加数据的验证，确保数据   getter方法获取属性   可以作其他处理
class Stu:
    def __init__ (self, name, age):
        self._name = name
        self._age = age
    def fun(self):
        print ('hello, the name is %s, the age is %d'%(self._name,self._age))

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if age > 0:
            self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return  self._age

p4 = Stu('tom', 20)
p4.fun()                            # hello, the name is tom, the age is 20

p4.set_age(30)
print (p4.get_age())

# 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象访问 p.__name 不能被访问
# 一般将一些私有属性（不希望被外部访问的属性）以_开头  使用_开头的属性是私有属性 一般不修改私有属性

# property装饰器，用来将一个get方法 转换为对象的属性 可以像调用属性一样使用get方法  使用property的方法必须和属性名是一样的
# setter方法的装饰器：@属性名.setter  必须在property后面 否则报错

class Stu1:
    def __init__ (self, name, age):
        self._name = name
        self._age = age
    def fun(self):
        print ('hello, the name is %s, the age is %d'%(self._name,self._age))
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return  self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age



p5 = Stu1('jerry', 11)
p5.fun()
print (p5.name)

p5.name = 'li'
p5.age = 22
p5.fun()
print (p5.name)

# =======================================================封装
# 继承可以直接让子类获取到父类的方法或属性 避免代码的重复性 符合OCP原则 过继承来对一个类进行扩展
# 子类中如果有和父类同名的方法，则通过子类实例去调用方法时 子类覆盖父类 也叫重写
# issubclass() 检查一个类是否是另一个类的子类
class AA:
    def ab(self):
        print ('this is father ab')
    def ac(self):
        print ('this is father ac')

class BA(AA):
    def bb(self):
        print ('this is son ba')
    def ab(self):
        print ('this is son ab')

b = BA()
b.ac()                                  #this is father ac
b.bb()                                  #this is son bb
b.ab()                                  #this is son ab

#  object是所有类的父类，所有类都继承自object
# 父类中的所有方法都会被子类继承，包括特殊方法，也可以重写特殊方法
# super() 可以用来获取当前类的父类，调用父类方法时，不需要传递self
# 在Python中是支持多重继承的，可以为一个类指定多个父类 在类名的()内添加多个类来实现多重继承 会是代码复杂 避免
st = Stu('xiaobai', 18)
st1 = Stu1('jack', 20)
def fun1(obj):
    if isinstance(obj,Stu1):
        print ('hello',obj.name)
    else:
        print ('not instance')

fun1(st)                                # not instance
fun1(st1)                               # hello jack


'''
类属性:直接在类中定义的属性是类属性 通过类或类的实例访问到 通过类或类的实例访问到
类属性只能通过类对象来修改，无法通过实例对象修改(知识修改了实例的对象的值）

实例属性:通过实例对象添加的属性属于实例属性 只能通过实例对象来访问和修改，类对象无法访问修改

实例方法:以self为第一个参数的方法，在调用时将调用对象作为self传入 可以通过实例和对象调用
    实例调用时，自动将调用对象作为self传入  类调用时，手动传入self

类方法: 在类内部使用 @classmethod 来修饰的方法 第一个参数是cls(当前类对象) 自动传递
类方法可以通过类去调用，也可通过实例调用 无区别

静态方法: 在类中使用 @staticmethod 来修饰的方法 不需要指定任何的默认参数，静态方法可以通过类和实例去调用
静态方法是一个和当前类无关的方法，只是一个保存到当前类中的函数
'''
class Doc:
    #类属性
    count = 0           #公有的类属性
    __age = 20          #私有的类属性 不可以在类外通过类对象或实例对象访问
    #实例属性
    def __init__(self):
        self.name = 'libai'
    #实例方法
    def slm(self):
        print('实例方法',self)
    #类方法
    @classmethod
    def clm(self):
        print ('类方法',self)
    #静态方法
    @staticmethod
    def stm():
        print ('静态方法')
#类属性
doc = Doc()                 #实例
doc.count = 100             #实例对象 只是改了此实例对象的值
print (doc.count)           #100
print (Doc.count)           #0
Doc.count = 90              #类对象
print (Doc.count)           #90
print (doc.count)           #100 doc已经实例化了

#实例属性
print (doc.name)            #libai
# print (Doc.name)          #错误 类对象不能访问修改实例属性

#实例方法   两个相等
doc.slm()                   #实例方法 <__main__.Doc object at 0x1067e8438>
Doc.slm(doc)                #实例方法 <__main__.Doc object at 0x1067e8438>

#类方法     两个相等
doc.clm()                   #类方法 <class '__main__.Doc'>
Doc.clm()                   #类方法 <class '__main__.Doc'>

#静态方法
doc.stm()                  #静态方法
Doc.stm()                  #静态方法

# 特殊方法
# def __del__(self):
#         print('类对象被删除了~~~',self)
# 在程序中没有被引用的对象就是垃圾 垃圾对象从内存中删除 Python中有自动的垃圾回收机制
# __str__()  会在尝试将对象转换为字符串的时候调用   可以用来指定对象转换为字符串的结果
# __repr__() 会在对当前对象使用repr()函数时调用 是指定对象在‘交互模式’中直接输出的效果
# __bool__() 通过bool来指定对象转换为布尔值的情况
# __gt__() 对象做大于比较的时候调用 两个参数，一个self表示当前对象，other表示和当前对象比较的对象
class Teacher:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Teacher [name = %s, age = %d]'%(self.name, self.age)

    def __repr__(self):
        return 'hello'

    def __bool__(self):
        return self.age >25

    def __gt__(self,other):
        return self.age > other.age

t1 = Teacher('xb',20)
t2 = Teacher('dj',30)
# 当我们打印一个对象时，实际上打印的是对象的中特殊方法 __str__()的返回值
print (t1)                       #Teacher [name = xb, age = 20]
print (t2)                       #Teacher [name = dj, age = 30]
print (repr(t1))                 #hello
# 函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式
print (repr('nihao'))            #'nihao'
print (str('nihao'))             #nihao
print (repr(1/7.0))              #0.14285714285714285
print (str(1/7.0))               #0.14285714285714285
print (t1 > t2)                  #False
print (bool(t1))                 #False

    # object.__add__(self, other)
    # object.__sub__(self, other)
    # object.__mul__(self, other)
    # object.__matmul__(self, other)
    # object.__truediv__(self, other)
    # object.__floordiv__(self, other)
    # object.__mod__(self, other)
    # object.__divmod__(self, other)
    # object.__pow__(self, other[, modulo])
    # object.__lshift__(self, other)
    # object.__rshift__(self, other)
    # object.__and__(self, other)
    # object.__xor__(self, other)
    # object.__or__(self, other)

    # object.__lt__(self, other) 小于 <
    # object.__le__(self, other) 小于等于 <=
    # object.__eq__(self, other) 等于 ==
    # object.__ne__(self, other) 不等于 !=
    # object.__gt__(self, other) 大于 >
    # object.__ge__(self, other) 大于等于 >=

    # __len__()


# =======================================================模块
# 模块化指将一个完整的程序分解为一个一个小的模块 在Python中一个py文件就是一个模块
# 1 import 模块名
# 2 import 模块名 as 模块别名
# 3 from 模块名 import 变量 as 别名
# 4 from 模块名 import *
# 引入同一个模块多次，模块的实例只会创建一个
# 在每一个模块内部都有一个__name__属性，可以获取到模块的名字 __name__属性值为 __main__的模块是主模块，一个程序中只会有一个主模块
print(__name__)

import test1 as ts1
print (ts1.a)

# =====================模块内
# 添加了_的变量只能在模块内部访问，在通过import引入时不会引入_开头的变量
# 适当利用 if __name__ == '__main__':  当被当作模块时 不会被执行

# =======================================================包
# 普通的模块就是一个py文件 包是一个文件夹
# 包中必须要一个一个 __init__.py 这个文件，这个文件中可以包含有包中的主要内容

# __pycache__ 是模块的缓存文件
# py代码在执行前，需要被解析器先转换为机器码，然后再执行
#   所以我在使用模块（包）时，也需要将模块的代码先转换为机器码然后再交由计算机执行
#   为了提高程序运行的性能，python会在编译过一次以后，将代码保存到一个缓存文件中
#   在下次加载模块（包）时，不再重新编译 直接加载缓存中编译好的代码


# =======================================================系统模块
# pprint 模块它提供一个方法 pprint() 该方法可以用来对打印的数据做简单的格式化
import pprint
# sys模块，提供一些变量和函数，可以获取到Python解析器的信息 或者通过函数来操作Python解析器
import sys

# sys.argv  执行代码时命令行中所包含的参数 该属性是一个列表，列表中保存了当前命令的所有参数
print (sys.argv)

# sys.modules 当前程序中引入的所有模块 是一个字典，字典的key是模块的名字，字典的value是模块对象
print (sys.modules)

# sys.path 是一个列表 列表中保存的是模块的搜索路径
print (sys.path)
pprint.pprint(sys.path)

# sys.platform 表示当前Python运行的平台
print(sys.platform)

# sys.exit() 用来退出程序
# sys.exit('exit!!!!!!')
# print('nice')

# os 模块让我们可以对操作系统进行访问
import os

# os.environ  可以获取到系统的环境变量
# pprint.pprint(os.environ())

# os.system() 可以用来执行操作系统的名字
os.system('ls')

# ===============================================异常操作
# 使用try语句 避免程序报错
''' try语句
        try:
            代码块（可能出现错误的语句）
        except NameError:
            代码块（出现错误以后的处理方式）
            print('NameError')
        except ZeroDivisionError:
            代码块（出现错误以后的处理方式）
        except IndexError:
            代码块（出现错误以后的处理方式）

# Exception 是所有异常类的父类 会捕获到所有的异常  如果except后不跟任何内容 也会捕获全部异常

        except Exception as e:
            print ('未知错误',e, type(e))
        else：
            代码块（没出错时要执行的语句）
        finally:
            代码块（该代码块总会执行）
        try必须有 else语句可以没有  except和finally至少有一个
'''
class MyError(Exception):
    pass

# raise用于向外部抛出异常，后边可以跟一个异常类，或异常类的实例   raise Exception
h = 1
# if h < 2:
#     raise MyError('小于2了。。。')    #File "py.py", line 355,  / in <module> raise MyError('小于2了。。。') /  __main__.MyError: 小于2了。。。

# ===============================================文件操作
# with ... as 语句 文件操作等只能在with中使用，一旦with结束则文件会自动close()
'''文件打开
使用open函数来打开一个文件  返回一个对象，这个对象就代表了当前打开的文件
open(file, mode='r', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
open()默认是以文本文档方式打开，默认的编码为None 一般指定编码 另一种为二进制文件（图片、mp3、ppt等这些文件）
mode:   r    只读 （默认）
        w w+ 可写的，文件存在会覆盖原有内容 文件不存在创建文件
        a a+ 追加内容, 文件不存在创建文件
        x    新建文件, 文件若存在报错
        r+   可读可写, 文件不存在报错
默认t 文本文档读取     b 读取二进制文件   ===> mode = rb 读取二进制文件
'''

'''文件读取
read()，用来读取文件中的内容，它会将内容全部保存为一个字符串返回 文件较大时 避免一次性读取 容易导致内存泄漏
read(​size​) 指定读取size的字节 默认为-1 全部读取     每一次读取都是从上次读取到位置开始读取的
readline() 可以用来读取一行内容   content = file_obj.readline()
readline() 一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回 contents = file_obj.readline()
'''


filename = 'test1.py'
try:
    with open(filename) as file_obj:
        content = file_obj.read(10)
        content = file_obj.read(10)
        content = file_obj.read(10)
        content = file_obj.read(10)
        content = file_obj.read(-1)              # 从上一行读取位置开始读
        print (content)
except FileNotFoundError:
    print (f'{filename}文件不存在')

# file_obj.close()
# 读取大文件
try:
    with open(filename) as file_obj:
        file_content = ''
        number = 10
        while True:
            content1 = file_obj.read(number)
            if not content1:
                break
            file_content += content1

except FileNotFoundError:
    print (f'{filename}文件不存在')
print(file_content)
# ===================其他操作
# seek() 可以修改当前读取的位置 两个参数(切换的位置, 计算方式) 计算方式:0==>从头计算(默认)  1==>当前位置  2==>最后开始计算
# tell() 方法用来查看当前读取的位置
# os.listdir() 获取指定目录的目录结构 需要一个路径作为参数，会获取到该路径下的目录结构，默认路径为当前目录
#              返回一个列表，目录中的每一个文件（夹）的名字都是列表中的一个元素
# os.getcwd() 获取当前所在的目录
# os.chdir() 切换当前所在的目录 作用相当于 cd
# os.mkdir() 创建目录
# os.rmdir() 删除目录
# os.remove()  删除文件
# os.rename('old_name','new_name') 可以对一个文件进行重命名，也可以用来移动一个文件
l = os.listdir()
m = os.getcwd()

pprint.pprint(l)
pprint.pprint(m)
