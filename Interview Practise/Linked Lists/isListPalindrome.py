#  https://app.codesignal.com/interview-practice/task/HmNvEkfFShPhREMn4

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseList(root):
    pre = None
    cur = root
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    
    return pre


def isListPalindrome(head):
    if not head:
        return True
        
    slow = head
    fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    slow = reverseList(slow)
    fast = head
    
    while slow:
        if slow.value != fast.value:
            return False
        slow = slow.next
        fast = fast.next
    
    return True
