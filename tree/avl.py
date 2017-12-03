import math
from queue import queue
from util import string


class TreeWrapper(object):
    def __init__(self):
        self.root = None
        self.height = 0

    def find_root(self, node):
        while node.parent is not None:
            node = node.parent

        return node

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)
            self.root = self.find_root(self.root)

        self.height = self.root.height

    def delete(self, value):
        self.root.delete(value)
        self.height = self.root.height

    def pretty_print(self):
        max_value = 0
        lines = []

        q = queue.Queue()
        q.enqueue((self.root, 0))

        s = ""
        current_depth = 0
        while q.length > 0:
            node, depth = q.dequeue()
            if depth != current_depth:
                current_depth = depth
                s += "\n%d" % node.value
            else:
                s += "%d" % node.value

            if node.left is not None:
                q.enqueue((node.left, depth + 1))

            if node.right is not None:
                q.enqueue((node.right, depth+ 1))

        print s


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)

            else:
                self.right = TreeNode(value)
                self.right.parent = self

        else:
            if self.left is not None:
                self.left.insert(value)

            else:
                self.left = TreeNode(value)
                self.left.parent = self

        lh = self.calculate_subtree_height(self.left)
        rh = self.calculate_subtree_height(self.right)

        self.height = max(lh, rh) + 1

        if abs(lh - rh) > 1:
            self.fixup(rh, lh)

    def delete(self, value):
        if value == self.value:
            isRightChild = False
            isRoot = False

            if self.parent is None:
                isRoot = True

            if self.parent is not None and self.parent.right == self:
                isRightChild = True

            if self.right is None and self.left is None:
                if isRightChild:
                    self.parent.right = None

                else:
                    self.parent.left = None

            elif self.right is not None and self.left is None:
                if isRightChild:
                    self.parent.right = self.right

                elif isRoot:
                    self.right.parent = None

                else:
                    self.parent.left = self.right

                self.right.parent = self.parent

            elif self.right is None and self.left is not None:
                if isRightChild:
                    self.parent.right = self.left

                elif isRoot:
                    self.left.parent = None

                else:
                    self.parent.left = self.left

                self.left.parent = self.parent

            else:
                s = self.successor()

                if s.parent.right == s:
                    s.parent.right = s.right

                else:
                    s.parent.left = s.right

                self.value = s.value

        elif value > self.value:
            if self.right is not None:
                self.right.delete(value)

            else:
                raise ValueError("value %d not found!" % value)

        else:
            if self.left is not None:
                self.left.delete(value)

            else:
                raise ValueError("value %d not found!" % value)

        lh = self.calculate_subtree_height(self.left)
        rh = self.calculate_subtree_height(self.right)

        self.height = max(lh, rh) + 1

        if abs(lh - rh) > 1:
            self.fixup(rh, lh)

    @staticmethod
    def calculate_subtree_height(subtree):
        if subtree is None:
            return -1

        if subtree.left is None:
            lh = -1

        else:
            lh = subtree.left.height

        if subtree.right is None:
            rh = -1

        else:
            rh = subtree.right.height

        return max(lh, rh) + 1

    def predecessor(self):
        predecessor = self.left

        if predecessor is not None:
            while predecessor.right is not None:
                predecessor = predecessor.right

        return predecessor

    def successor(self):
        successor = self.right

        if successor is not None:
            while successor.left is not None:
                successor = successor.left

        return successor

    def right_rotate(self):
        old_parent = self.parent
        if self.parent is not None:
            if self.parent.right == self:
                self.parent.right = self.left


            else:
                self.parent.left = self.left

        self.left.parent = self.parent

        self.parent = self.left
        lr = self.left.right
        self.left.right = self
        self.left = lr

        promote = self.left
        self.left = promote.right
        if promote.right is not None:
            promote.right.parent = self

        promote.right = self

        self.height = max(self.calculate_subtree_height(self.left), self.calculate_subtree_height(self.right)) + 1
        promote.height = max(self.calculate_subtree_height(promote.left), self.calculate_subtree_height(promote.right)) + 1
        if old_parent is not None:
            old_parent.height = max(self.calculate_subtree_height(old_parent.left), self.calculate_subtree_height(old_parent.right)) + 1

    def left_rotate(self):
        old_parent = self.parent
        if self.parent is not None:
            if self.parent.right == self:
                self.parent.right = self.right

            else:
                self.parent.left = self.right

        self.right.parent = self.parent

        promote = self.right
        self.right = promote.left
        if promote.left is not None:
            promote.left.parent = self

        self.parent = promote
        promote.left = self

        self.height = max(self.calculate_subtree_height(self.left), self.calculate_subtree_height(self.right)) + 1
        promote.height = max(self.calculate_subtree_height(promote.left), self.calculate_subtree_height(promote.right)) + 1

        if old_parent is not None:
            old_parent.height = max(self.calculate_subtree_height(old_parent.left), self.calculate_subtree_height(old_parent.right)) + 1

    def fixup(self, rh, lh):
        if rh > lh:
            rrh = (lambda: 0 if self.right.right is None else self.right.right.height)()
            rlh = (lambda: 0 if self.right.left is None else self.right.left.height)()

            if rrh >= rlh:
                self.left_rotate()
            else:
                self.right.right_rotate()
                self.left_rotate()

        else:
            llh = (lambda: 0 if self.left.left is None else self.left.left.height)()
            lrh = (lambda: 0 if self.left.right is None else self.left.right.height)()
            if llh >= lrh:
                self.right_rotate()

            else:
                self.left.left_rotate()
                self.right_rotate()

if __name__ == "__main__":
    tree = TreeWrapper()

    for i in range(1, 11):
        print "insert: %d" % i
        tree.insert(i)
        tree.pretty_print()

    print "delete: %d" % 4
    tree.delete(4)
    tree.pretty_print()


