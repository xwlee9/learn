# nums = []
# a = 0
# b = 1
# for _ in range(10):
#     nums.append(a)
#     a, b = b, a+b

# for num in nums:
#     print(num)

class Fibonacci(object):
    def __init__(self, ite):
        self.nums = list()
        self.count = 0
        self.a = 0
        self.b = 1
        self.ite = ite

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.ite:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return ret
        else:
            raise StopIteration

fb = Fibonacci(10)

for num in fb:
    print (num)

