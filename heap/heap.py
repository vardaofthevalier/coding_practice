import math


class BinaryHeap(object):
    def __init__(self, ordering, elems=None):
        self.orderingProperty = None

        if ordering == "min":
            self.orderingProperty = lambda a, b: True if a < b else False

        elif ordering == "max":
            self.orderingProperty = lambda a, b: True if a > b else False

        else:
            raise ValueError

        self.rep = []
        self.size = 0
        if elems is not None:
            self.heapify(elems)
            self.size = len(elems)

    def heapify(self, elems):
        for e in elems:
            self.insert(e)

    def insert(self, item):
        self.rep.append(item)

        if self.size > 0:
            self._siftUp()

        self.size += 1

    def extract(self):
        item = self.rep[0]
        self.rep[0] = self.rep.pop()
        self._siftDown()
        self.size -= 1

        return item

    def peek(self):
        return self.rep[0]

    def isEmpty(self):
        if self.size == 0:
            return True

        else:
            return False

    def _siftUp(self):
        idx = len(self.rep) - 1
        current = self.rep[idx]
        parent = self.rep[idx / 2]

        while self.orderingProperty(current, parent):
            self.rep[idx/2] = current
            self.rep[idx] = parent

            idx = idx / 2
            current = self.rep[idx]
            parent = self.rep[idx / 2]

    def _siftDown(self):
        idx = 0
        l = 1
        r = 2

        temp = self.rep[idx]
        while idx <= len(self.rep) - 1:
            if not self.orderingProperty(self.rep[idx], self.rep[l]) and not self.orderingProperty(self.rep[idx], self.rep[r]):
                if self.orderingProperty(self.rep[l], self.rep[r]):
                    self.rep[idx] = self.rep[l]
                    self.rep[l] = temp
                    idx = l


                else:
                    self.rep[idx] = self.rep[r]
                    self.rep[r] = temp
                    idx = r

            else:
                break

            l = idx * 2
            r = (idx * 2) + 1
            temp = self.rep[idx]

    def pretty_print(self):
        maxDepth = int(math.log(self.size, 2))
        maxWidth = 2**int(maxDepth) * 3
        lines = []

        d = 0
        i = 0
        while d <= maxDepth:
            items = 2**d
            middleSpaces = items - 1
            justify = (maxWidth - middleSpaces) / 2
            line = "".ljust(justify, " ")
            j = 0
            while j < items and i < self.size:
                line += "%d " % self.rep[i]
                i += 1
                j += 1

            lines.append(line)
            d += 1

        for l in lines:
            print l




if __name__ == "__main__":
    # min heap
    elems = range(1, 11)
    # minHeap = BinaryHeap("min", elems)
    #
    # print minHeap.rep
    #
    # minHeap.insert(6)
    #
    # minHeap.pretty_print()
    #
    # minHeap.insert(3)
    #
    # minHeap.pretty_print()
    #
    # minHeap.insert(16)
    #
    # minHeap.pretty_print()

    maxHeap = BinaryHeap("max", elems)

    maxHeap.pretty_print()