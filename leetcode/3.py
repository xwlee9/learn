class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = list(s)
        b = len(a)
        c = a.copy()
        for i in range(b):
            c[i] = -1
        loc = -1
        res = 0
        l = dict(zip(a, c))
        for i in range(b):
            loc = max(loc,l[a[i]])
            l.update({a[i]:i})
            res = max(res,i-loc)
        return res

