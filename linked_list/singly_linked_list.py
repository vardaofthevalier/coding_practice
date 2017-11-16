class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.color = None

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

        current = self.head
        i = 0
        while i < idx:
            current = current.next
            i += 1

        return current.value

    def __setitem__(self, idx, value):
        if idx > self.length - 1:
            raise IndexError

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

    def insert(self, idx, node):
        if self.length == 0:
            self.head = node

        elif idx > self.length - 1:
            raise IndexError

        else:
            current = self.head
            prev = None
            i = 0
            while i < idx:
                prev = current
                current = current.next
                i += 1

            node.next = current

            if prev is not None:
                prev.next = node

            if i == 0:
                self.head = node

        self.length += 1

    def remove(self, idx):
        del self[idx]

    def partition(self, x):
        x_node = SinglyLinkedListNode(x)
        l_neighbor = None
        l_head = x_node
        r_neighbor = None
        r_tail = x_node

        current = self.head
        while current is not None:
            if current.value >= x:
                next = current.next
                r_tail.next = current
                if r_neighbor is None:
                    r_neighbor = current
                r_tail = current

            else:
                next = current.next
                current.next = l_head
                if l_neighbor is None:
                    l_neighbor = current
                l_head = current

            current = next

        l_neighbor.next = r_neighbor
        x_node.next = None
        self.head = l_head

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


def sum_lists(a, b):
    if len(a) > len(b):
        lg = a.head
        sm = b.head

    else:
        lg = b.head
        sm = a.head

    result = SinglyLinkedList()
    carry = None

    while sm is not None:
        sum = sm.value + lg.value
        if carry is not None:
            sum += carry

        if sum < 10:
            set = SinglyLinkedListNode(sum)

        else:
            set = SinglyLinkedListNode(sum % 10)
            carry = sum / 10

        result.insert(0, set)
        sm = sm.next
        lg = lg.next

    while lg != None:
        sum = lg.value
        if carry != None:
            sum += carry

        if sum < 10:
            set = SinglyLinkedListNode(sum)

        else:
            set = SinglyLinkedListNode(sum % 10)
            carry = sum / 10

        result.insert(0, set)
        lg = lg.next

    return result

if __name__ == "__main__":
    # l = SinglyLinkedList()
    #
    # for v in range(1, 11):
    #     l.insert(0, v)
    #
    # l.pretty_print()
    #
    # print l.head.value
    #
    # l.remove(0)
    #
    # l.pretty_print()
    #
    # print l.head.value
    #
    # for k in range(0, len(l)):
    #     print l[k]
    #
    # print l[-1]
    #
    # l.partition(5)
    #
    # l.pretty_print()

    n1 = [1, 9, 5, 1]
    l1 = SinglyLinkedList()
    n2 = [3, 9, 5]
    l2 = SinglyLinkedList()

    for n in n1:
        node = SinglyLinkedListNode(n)
        l1.insert(0, node)

    l1.pretty_print()

    for n in n2:
        node = SinglyLinkedListNode(n)
        l2.insert(0, node)

    l2.pretty_print()

    s = sum_lists(l1, l2)

    s.pretty_print()






