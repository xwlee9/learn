import time
from collections import Iterable
from collections import Iterator


# 迭代器 : 也可以用在类型转换 tuple ==> list
class People(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,names):
        self.names.append(names)

    def __iter__(self):  # 一个对象成为可以迭代的对象 可以使用for 那么必须实现 __iter__  方法
        # return PeopleIterator(self)
        return self
    def __next__(self):  # 迭代器 有__iter__ 和 __next__ 方法
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration  # 自定义抛出异常
    


# class PeopleIterator(object):
#     def __init__(self,obj):
#         self.obj = obj
#         self.current_num = 0
    
#     def __iter__(self):
#         pass

#     def __next__(self):
#         if self.current_num < len(self.obj.names):
#             ret = self.obj.names[self.current_num]
#             self.current_num += 1
#             return ret
#         else:
#             raise StopIteration  

p = People()
p.add("jack")
p.add("rose")
p.add("tom")

print("People 是可迭代对象", isinstance(p,Iterable))  
p_ite = iter(p)
print("p_ite 是迭代器", isinstance(p_ite,Iterator))
# print(next(p_ite))

for name in p:
    print(name)
    time.sleep(1) 
