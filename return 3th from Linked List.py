class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def get_nth_node(head, n):
    current = head
    count = 0

    while current is not None:
        if count == n:
            return current
        count += 1
        current = current.next

    return None  # Return None if the index is out of bounds

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

index_to_get = 2  # Third node (index 2)

third_node = get_nth_node(head, index_to_get)

if third_node is not None:
    print(f"Value of the third node: {third_node.value}")
else:
    print(f"Index {index_to_get} is out of bounds.")
