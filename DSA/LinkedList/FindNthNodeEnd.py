#Program to Find Nth Node from the End in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findNthFromEnd(head: ListNode, n: int) -> ListNode:
    fast = head
    slow = head
    
    for _ in range(n):
        if not fast:
            return None
        fast = fast.next
        

    while fast:
        fast = fast.next
        slow = slow.next

    return slow
