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
    
# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
