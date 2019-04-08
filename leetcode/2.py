# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        a1 = ListNode(0)
        a = a1
        carry = 0
        while (l1 or l2):
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0 
            add = num1 + num2 + carry
            a.next = ListNode(add % 10) # 取余数 反过来 
            carry = add //10 # 判断进位
            a = a.next
            if l1 :
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry>0: # 判断最高一位是不是依旧有进位
            a.next = ListNode(1) 
        return a1.next # a指向链表的尾部 a1指向链表的头部