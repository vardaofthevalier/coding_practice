# stack is basically a linked list with the following methods: push(item), pop(), peek(), isEmpty()


class StackNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, item):
        n = StackNode(item)
        if self.length == 0:
            self.head = n

        else:
            n.next = self.head
            self.head = n

        self.length += 1

    def pop(self):
        item = self.head.value
        self.head = self.head.next
        self.length -= 1
        return item

    def peek(self):
        if self.length == 0:
            raise IndexError

        return self.head.value

    def isEmpty(self):
        if self.length == 0:
            return True

        else:
            return False

    def pretty_print(self):
        delim = " => "
        rep = []

        current = self.head
        i = 0
        while i < self.length:
            rep.append(current.value)
            current = current.next
            i += 1

        print delim.join(map(lambda x: str(x), rep))

if __name__ == "__main__":
    stack = Stack()
    print stack.isEmpty()
    for x in range(1, 11):
        stack.push(x)

    stack.pretty_print()

    print stack.peek()
    stack.pop()
    stack.pretty_print()
    print stack.isEmpty()


