class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def addLast(self, other):
        node = ListNode(0)
        node.next = self

        while node.next is not None:
            node = node.next
            if node.next is None:
                node.next = ListNode(other)
                break

        return self

    def addFirst(self, other):
        self.next = ListNode(self.val, self.next)
        self.val = other

        return self

    def __str__(self):
        return f"{self.val} -> {self.next}"


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(0).addLast(1)
print(l3)
l3.addLast(4)
print(l3)
l3.addFirst(-1)
print(l3)
print(l1)
print(l2)
