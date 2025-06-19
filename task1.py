class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next

    # Reverse
    def reverse_list(self):
        prev = None
        current = self.head
        # print(current.data)
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Sort
    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return self._sorted_merge(left, right)

    def _get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

    # Merge two lists
    def merge_sorted_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next


# List 1 create
slist1 = SinglyLinkedList()
slist1.push(1)
slist1.push(9)
slist1.push(5)

# List 1 operations
print("List 1 at start of operations:")
slist1.print_list()

print("\nList 1 after REVERSE operation:")
slist1.reverse_list()
slist1.print_list()

print("\nList 1 after SORT operation:")
slist1.sort()
slist1.print_list()


# List 2 create
slist2 = SinglyLinkedList()
slist2.push(10)
slist2.push(-5)
slist2.push(25)

# List 2 operations
print("\nList 2 at start of operations:")
slist2.print_list()

print("\nList 2 after REVERSE operation:")
slist2.reverse_list()
slist2.print_list()

print("\nList 2 after SORT operation:")
slist2.sort()
slist2.print_list()

# Merge lists
merged_list = SinglyLinkedList()
merged_list.head = merged_list.merge_sorted_lists(slist1.head, slist2.head)
print("\nMerged sorted list:")
merged_list.print_list()
