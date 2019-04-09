class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        a = list(s)
        n = len(a)
        l = []                                              # j                j
        size = 2 * numRows -2 # 切割成块                      i0 i1 
        for i in range(numRows): # 用行大小做小块遍历   #     || L E E D \ C O  || D E I S \H I || R I N G ||  
            for j in range(i,n,size):  # 直接遍历每个小块的i个位置
                l.append(a[j])               
                temp = j + size - 2*i  # j - i + size - i
                if (i != 0) and (i != numRows -1) and (temp < n):
                    l.append(a[temp])
        return "".join(l)