import unittest
from data_structures.linkedlist import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_add_first(self):
        test_node_1 = ListNode(0)
        test_node_1.addLast(1)
        expected_answer_1 = ListNode(0, ListNode(1))
        self.assertEqual(test_node_1.__str__(), expected_answer_1.__str__())


if __name__ == '__main__':
    unittest.main()
