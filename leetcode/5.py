class Solution:
    def SearchP(self, a, lift, right, start, maxn, n):
        while (lift >= 0 and right < n and a[lift] == a[right]):
            lift -= 1
            right += 1
            # print(lift)
        if (maxn < right - lift - 1): # 若没有执行 while ==> false 若执行了while l-- r++ ===> 长度为r-l-2+1
            start = lift + 1  # while循环中 若上一次满足 执行了 l-- 这次不满足 加回来来
            maxn = right -lift - 1
        return start, maxn

    def longestPalindrome(self, s: str) -> str:
        # 以每一个字符为中心，像两边扩散来寻找回文串
        a = list(s)
        n = len(a)
        if n == 0:
            return ""
        if 0< n < 2:
            return a[0]
        maxn = 0
        start = 0
        for i in range(n-1): # 没有必要单独再遍历 a[n-1]
                start,maxn = self.SearchP(a, i, i, start, maxn, n)  # 奇数的时候
                # print(i,start)
                start,maxn = self.SearchP(a, i, i+1, start, maxn, n) # 偶数数的时候 遍历两遍，
            # print(a[start:maxn])
        return "".join(a[start:(start+maxn)])
    