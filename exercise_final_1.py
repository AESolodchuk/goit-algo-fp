class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def insertion_sort(self):
        if self.head is None:
            return

        sorted_head = None
        cur = self.head

        while cur:
            nxt = cur.next
            sorted_head = self.sorted_insert(sorted_head, cur)
            cur = nxt

        self.head = sorted_head

    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            sorted_head = new_node
        else:
            cur = sorted_head
            while cur.next is not None and cur.next.data < new_node.data:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

        return sorted_head

    def __str__(self):
        l = []
        cur = self.head
        while cur:
            l.append(cur.data)
            cur = cur.next
        return str(l)


def merge_lists(list1, list2):

    merged_list = LinkedList()

    cur_node1 = list1.head
    cur_node2 = list2.head

    while cur_node1 and cur_node2:

        if cur_node1.data < cur_node2.data:
            merged_list.insert_at_end(cur_node1.data)
            cur_node1 = cur_node1.next

        else:
            merged_list.insert_at_end(cur_node2.data)
            cur_node2 = cur_node2.next

    while cur_node1:
        merged_list.insert_at_end(cur_node1.data)
        cur_node1 = cur_node1.next
    while cur_node2:
        merged_list.insert_at_end(cur_node2.data)
        cur_node2 = cur_node2.next

    return merged_list


def result():
    first = [1, 2, 3, 4, 5]
    second = [6, 7, 8, 9, 10]

    lf = LinkedList()
    ls = LinkedList()

    [lf.insert_at_end(i) for i in first]
    [ls.insert_at_end(i) for i in second]

    print("Початкові списки:")
    print(f"Перший список: {lf}")
    print(f"Другий список: {ls}")

    lf.reverse()
    ls.reverse()
    print(f"\nРеверсування списків:")
    print(f"Перший список: {lf}")
    print(f"Другий список: {ls}")

    lf.insertion_sort()
    ls.insertion_sort()
    print(f"\nCортування списків:")
    print(f"Перший список: {lf}")
    print(f"Другий список: {ls}")

    merged_list = merge_lists(lf, ls)
    print(f"\nОб'єднання списків:")
    print(merged_list)


result()
