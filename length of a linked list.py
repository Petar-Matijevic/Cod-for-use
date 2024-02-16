class ListNode:
    def __init__(self,value=0,next=None):
        self.vale=value
        self.next=next

def get_linked_list_length(head):
    length=0
    current=head

    while current != None:
        length+=1
        current=current.next
    return length
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

length = get_linked_list_length(head)
print("Length of the linked list:", length)