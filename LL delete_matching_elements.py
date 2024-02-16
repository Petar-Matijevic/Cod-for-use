class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

def delete_matching_elements(head,target_value):
    # Handel wher first is matching tre
    while head is not None and head.value == target_value:
        head = head.next

    current = head
    prev = None

    while current is not None:
        if current.value == target_value:
            # Remove up pint
            prev.next = current.next
            current=current.next
        else:
            prev = current
            current=current.next

    return  head

head = ListNode(3, ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5))))))

target_value = 3
print("Original linked list:")
current_node = head
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

# Delete nodes with the target value
head = delete_matching_elements(head, target_value)

print("\nLinked list after deleting nodes with value", target_value, ":")
current_node = head
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")