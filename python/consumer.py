from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "jack": "male",
    "rose": "female"
}

def my_chain(*args, **kwargs):
    for ite in args:
        yield from ite  # 等于下面两句
        # for value in ite:
        #     yield value

for value in my_chain(my_list, my_dict, range(5)):
    # print (value)
    pass

def g1(iterable):
    yield range(10)  # 只是会打印 range(0,10)



def g2(iterable):
    yield from range(10) # yield from 会得到迭代器产生的每一个值

for value in g1(range(10)):
    print(value)

for value in g2(range(10)):
    print(value)


# # 将多个生成器连接起来

def bottom():
    return (yield 42)

def middle():
    return (yield from bottom())

def top():
    return (yield from middle())

# 获取生成器
gen = top()
value = next(gen)
print(value)  # Prints '42'.
try:
    value = gen.send(value * 2)  # 传入 yield 的返回值 42 * 2
except StopIteration as exc:
    value = exc.value
print(value)  # Prints '84'.
