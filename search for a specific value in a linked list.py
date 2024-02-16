class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def search_in_linked_list(head, target_value):
    current = head
    while current != None:
        if current.value == target_value:
            return True
        current = current.next

    return False
# list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

target_value = 4
found = search_in_linked_list(head, target_value)

if found:
    print(f"Value {target_value} found in the linked list.")
else:
    print(f"Value {target_value} not found in the linked list.")