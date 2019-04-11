class Solution:
    def myAtoi(self, str: str) -> int:
        flag = 1
        tag = 0
        res = 0
        a = list(str)
        n = len(a)
        i = 0
        while i < n and a[i] == " ":
                i += 1
        if i < n :
            if a[i] == "+": 
                flag = 1
                tag += 1
            if a[i] == "-": 
                flag = -1
                tag += 1
        if tag != 0 : i += tag
        if i > n: 
            return 0
        while i < n and str[i] >= '0' and str[i] <= '9':
            res = 10 * res + int(a[i])
            if (res >= (2**31-1) and flag == 1): return (2**31 -1)
            if (res >= (2**31) and flag == -1): return -(2**31)
            i += 1
            # print (res)
        return res*flag