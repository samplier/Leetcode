# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mass= []
        slow = head
        while (slow!=None):
            mass.append(slow.val)
            # print (slow.val)
            slow = slow.next
        # print (mass)
        start = 0
        fin = len(mass)-1
        otv = True
        # print (mass[start])
        # print (mass[fin])
        while fin - start > 1:
            if (mass[start] == mass[fin]):
                start += 1
                fin -= 1
                # print(start)
                # print(fin)
            else:
                otv = False
                break
        if (mass[start] != mass[fin]):
            otv = False
        return otv