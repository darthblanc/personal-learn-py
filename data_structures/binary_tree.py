def simplify_traverse(path):
    rv = ""
    print(path)
    path.split(" ")

    for p in path:
        if p == ' ' or len(p) == 0:
            continue
        rv += p

    return rv


class BinaryTree(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def add(self, other):
        if self.val is None:
            self.val = other

        else:
            if other <= self.val and self.left is None:
                self.left = BinaryTree(other, None, None)

            elif other > self.val and self.right is None:
                self.right = BinaryTree(other, None, None)

            else:
                if other <= self.val and self.left is not None:
                    self.left.add(other)

                elif other > self.val and self.right is not None:
                    self.right.add(other)

    def remove(self, other):
        if self.val is None:
            raise Exception("Value does not exist")

        elif self.val == other:
            if self.left is not None:
                self.val = self.left.val
                self.left = self.left.left
            else:
                self.val = self.right.val
                self.right = self.right.right

        else:
            if other <= self.val and self.left is not None:
                self.left.remove(other)

            elif other > self.val and self.right is not None:
                self.right.remove(other)

    def preorder_traverse(self):
        if self.val is None:
            return ""

        left = ""
        if self.left is not None:
            left = self.left.preorder_traverse()

        right = ""
        if self.right is not None:
            right = self.right.preorder_traverse()

        return f"{self.val} {left} {right}"

    def postorder_traverse(self):
        if self.val is None:
            return ""

        left = ""
        if self.left is not None:
            left = self.left.postorder_traverse()

        right = ""
        if self.right is not None:
            right = self.right.postorder_traverse()

        return f"{left} {right} {self.val}"

    def inorder_traverse(self):
        if self.val is None:
            return ""

        left = ""
        if self.left is not None:
            left = self.left.inorder_traverse()

        right = ""
        if self.right is not None:
            right = self.right.inorder_traverse()

        return f"{left} {self.val} {right}"

    def __str__(self):
        return f"node: [val->{self.val} left->{self.left} , right->{self.right}]"


b = BinaryTree(None, None, None)
# b.add(1)
# b.add(1)
# b.add(5)
# b.add(2)
# b.add(0)
b.add(100)
b.add(20)
b.add(200)
b.add(10)
b.add(30)
b.add(150)
b.add(300)
print(b.preorder_traverse())
print(b.postorder_traverse())
print(b.inorder_traverse())
print(b)
b.remove(5)
# b.add(5)
print(b)
