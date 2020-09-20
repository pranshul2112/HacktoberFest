#  https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):

    head = l
    pre = None 
    while head and head.value == k:
        l = head.next 
        head = l
    
    while head: 
        while head and head.value != k:
            pre = head
            head = head.next 
          
        if head == None:
            return l
            
        pre.next = head.next
        
        head = pre.next
    
    return l  
            
