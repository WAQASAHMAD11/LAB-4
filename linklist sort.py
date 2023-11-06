class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sort(head):
    if not head or not head.next:
        return head
    mid = find_middle(head)
    left_half, right_half = head, mid.next
    mid.next = None

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    sorted_list = merge(left_half, right_half)
    return sorted_list

def find_middle(head):
    if not head:
        return None

    slow_ptr = head
    fast_ptr = head

    while fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.value < right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    current.next = left or right

    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
head = ListNode(arr[0])
current = head
for value in arr[1:]:
    current.next = ListNode(value)
    current = current.next

sorted_head = merge_sort(head)
print_linked_list(sorted_head)
