
# nums = [x**2 for x in range(10)] # 返回列表
# print(nums)
""" 生成器  是一种特殊的迭代器"""
# nums = (x**2 for x in range(10))  #  生成器 
# print(nums)
# for num in nums:
#     print (num)

def Fibonacci(ite):
    # print("---------1----------")  # test
    a, b = 0, 1
    count = 0
    while count < ite:
        # print("---------2----------")  # test
        # print(a)
        yield a  # 如果一个函数中有yield 语句 那么这个不是函数 是一个生成器的模版
        # print("---------3----------")  # test
        a, b = b, a+b
        count += 1
        # print("---------4----------")  # test
    return "nice!!!"

# 如果在调用function中 发现function中有yield 那么此时不是在调用函数 而是创建一个生成器的对象
obj = Fibonacci(10)
obj1 = Fibonacci(3)  # 两个对象不互相影响
for num in obj:
    print (num) # 执行到yield的时候 暂停 那么返回yield后面的值 不往下执行 知道第二次迭代的时候再往下执行
                # 看上去暂停执行 仍会继续执行

# while True:
#     try:
#         print(next(obj1))    
#     except Exception as ret:  # 捕获返回值 
#         print (ret.value)       
#         break

obj2 = Fibonacci(2)
print (next(obj2))
ret = obj2.send("good")  # 可以传入值的next() 就是传入yield a 的返回值 不可以第一次传入值 可以用send(None)
print (ret) # 结果是下一次调用yield yield后面的值
obj2.close() # 如果close()下面还有yield 会抛出异常 

obj3 = Fibonacci(3)
print (next(obj3))
obj.throw(Exception, "ERROR")  # 手动抛出一个异常 在第一个yield的地方抛出异常


