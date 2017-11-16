class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        if idx > self.length - 1:
            raise IndexError

        elif idx < 0:  # negative indexing support
            if self.length + idx < 0:
                raise IndexError

            else:
                idx = self.length + idx

        if self.length - idx < idx:
            current = self.tail
            i = self.length - 1
            while i > idx:
                current = current.previous
                i -= 1

        else:
            current = self.head
            i = 0
            while i < idx:
                current = current.next
                i += 1

        return current.value

    def __setitem__(self, idx, value):
        if idx > self.length - 1:
            raise IndexError

        if self.length - idx < idx:
            current = self.tail
            i = self.length - 1
            while i > idx:
                current = current.previous
                i -= 1

        else:
            current = self.head
            i = 0
            while i < idx:
                current = current.next
                i += 1

        current.value = value

    def __delitem__(self, idx):
        if self.length == 0:
            raise IndexError
        elif idx > self.length - 1:
            raise IndexError
        else:
            if self.length - idx < idx:
                current = self.tail
                prev = None
                i = self.length - 1
                while i > idx:
                    prev = current
                    current = current.previous
                    i -= 1

                if prev is None:
                    self.tail = current.previous

                else:
                    prev.previous = current.previous

            else:
                current = self.head
                prev = None
                i = 0
                while i < idx:
                    prev = current
                    current = current.next
                    i += 1

                if prev is None:
                    self.head = current.next

                else:
                    prev.next = current.next

            self.length -= 1

    def insert(self, idx, value):
        if self.length == 0:
            self.head = DoublyLinkedListNode(value)
            self.tail = self.head

        elif idx > self.length - 1:
            raise IndexError

        else:
            if self.length - idx < idx:
                current = self.tail
                i = self.length - 1
                while i > idx:
                    current = current.previous
                    i -= 1

                new = DoublyLinkedListNode(value)
                new.next = current
                new.previous = current.previous

                if current.previous is not None:
                    current.previous.next = new

                current.previous = new

                if i == self.length - 1:
                    self.tail = new

            else:
                current = self.head
                i = 0
                while i < idx:
                    current = current.next
                    i += 1

                new = DoublyLinkedListNode(value)
                new.next = current
                new.previous = current.previous

                if current.previous is not None:
                    current.previous.next = new

                current.previous = new

                if i == 0:
                    self.head = new

        self.length += 1

    def remove(self, idx):
        del self[idx]

    def pretty_print(self):
        delim = " <=> "
        rep = []

        current = self.head
        i = 0
        while i < self.length:
            rep.append(current.value)
            current = current.next
            i += 1

        print delim.join(map(lambda x: str(x), rep))

if __name__ == "__main__":
    l = DoublyLinkedList()

    for v in range(1, 11):
        l.insert(0, v)

    l.pretty_print()

    print l.head.value

    l.remove(0)

    l.pretty_print()

    print l.head.value

    for k in range(0, len(l)):
        print l[k]

    print l[-1]




