class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer=slow_pointer.next
        fast_pointer=fast_pointer.next.next

    return  slow_pointer
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

middle_node = find_middle_node(head)
print("Middle node value:", middle_node.value)