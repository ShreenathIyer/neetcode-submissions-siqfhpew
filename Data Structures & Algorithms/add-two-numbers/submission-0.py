# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, currSum = 0, 0
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            currSum = l1.val + l2.val + carry
            # print(currSum)
            carry, currVal = divmod(currSum, 10)
            # print(currVal)
            # print(carry)
            dummy.next = ListNode(currVal)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            currSum = l1.val + carry
            carry, currVal = divmod(currSum, 10)
            dummy.next = ListNode(currVal)
            dummy = dummy.next
            l1 = l1.next

        while l2:
            currSum = l2.val + carry
            carry, currVal = divmod(currSum, 10)
            dummy.next = ListNode(currVal)
            dummy = dummy.next
            l2 = l2.next
        
        while carry:
            dummy.next = ListNode(carry)
            dummy = dummy.next
            carry = 0

        return head.next

        