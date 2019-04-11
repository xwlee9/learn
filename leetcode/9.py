class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = 0
        x_t = x
        while(x_t > 0):
            temp = temp*10 + x_t%10
            x_t = x_t//10
        if (x == temp)
            return True
        else:
            return False