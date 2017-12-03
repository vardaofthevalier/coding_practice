# queue is basically a linked list with the following methods: enqueue(item), dequeue(), peek(), isEmpty()


class QueueNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, item):
        n = QueueNode(item)
        if self.length == 0:
            self.head = n
            self.tail = n

        else:
            self.tail.next = n
            self.tail = n

        self.length += 1

    def dequeue(self):
        item = self.head.value
        self.head = self.head.next
        self.length -= 1
        return item

    def peek(self):
        if self.length == 0:
            return None

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
    q = Queue()
    print q.isEmpty()
    for x in range(1, 11):
        q.enqueue(x)
        q.pretty_print()

    q.pretty_print()

    print q.peek()
    q.dequeue()
    q.pretty_print()
    print q.isEmpty()


