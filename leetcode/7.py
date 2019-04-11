class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        while(x != 0 ):
            res = res * 10 + x % 10
            x = x // 10
        if flag == 1:
            if res > 2 ** 31:
                return 0
            return -res
        else:
            if res > 2 ** 31-1:
                return 0
            return res