class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.size = self._find_current_size()

    def _find_current_size(self):
        node = self
        size = 1

        while node.next is not None:
            node = node.next
            size += 1

        return size

    def slice(self, i, j):
        node = self
        sequence_num = 0
        rv = ListNode(0)

        if j > len(self):
            j = len(self) + 1

        while sequence_num < j:
            if node is None:
                break
            if i <= sequence_num:
                rv.addLast(node.val)
            sequence_num += 1
            node = node.next

        return rv.next

    def addLast(self, item):
        node = ListNode(0)
        node.next = self

        while node.next is not None:
            node = node.next
            if node.next is None:
                node.next = ListNode(item)
                break

        self.size += 1

    def addFirst(self, item):
        self.next = ListNode(self.val, self.next)
        self.val = item
        self.size += 1

    def count(self, item):
        rv = ListNode(0)
        rv.next = self
        node = rv
        count = 0

        while node.next is not None:
            if node.next.val == item:
                count += 1
            node = node.next

        return count

    def remove(self, entry):
        node = ListNode(0)
        node.next = self

        while node.next is not None:
            if node.next.val == entry:
                node.next = node.next.next
                self.size -= 1
                break
            else:
                node = node.next

    def remove_all(self, entry):
        rv = ListNode(0)
        rv.next = self
        node = rv
        while node.next is not None:
            if node.next.val == entry:
                node.next = node.next.next
                self.size -= 1
            else:
                node = node.next

    def __contains__(self, item):
        rv = ListNode(0)
        rv.next = self
        node = rv
        while node.next is not None:
            if node.next.val == item:
                return True
            else:
                node = node.next

        return False

    def __len__(self):
        return self.size

    def __str__(self):
        return f"{self.val} -> {self.next}"


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    print(l1.count(1))
    # print(l1.slice(0, 1))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    # l3 = ListNode(0).addLast(1)
    l1.addLast(2)
    # print(len(l1))
    l2.addLast(9)
    l2.addFirst(8)
    # print(l2)
    # print(len(l2))
    # print(l3)
    # l3.addLast(4)
    # # print(l3)
    # l3.addFirst(-1)
    # # print(l3)
    # l1.addLast(2)
    # l1.addLast(2)
    # print(l1)
    # # l1.remove(2)
    # print(l1.__contains__(100))
    # # l1.remove_all(2)
    # print(l1)
    # print(l2)
    l4 = ListNode(0)
    l4.addLast(1)
    l4.addLast(2)
    print(l4.slice(1, 4))
    # print(len(l4))
