import queue
import stack


class Graph(object):
    def __init__(self, ):
        self.root_nodes = []

    def bfs(self, value):
        q = queue.Queue()
        for r in self.root_nodes:
            q.enqueue(r)

        while len(q) > 0:
            current = q.dequeue()

            if current.value == value:
                return current

            for n in current.neighbors:
                q.enqueue(n)

        return None

    def dfs(self, value):
        s = stack.Stack()
        for r in self.root_nodes:
            s.push(r)

        while len(s) > 0:
            current = s.pop()

            if current.value == value:
                return current

            for n in current.neighbors:
                s.push(n)

        return None

    def shortest_path(self, node1, node2):
        # unweighted shortest path
        q = queue.Queue()

        node1.distance = 0
        q.enqueue(node1)

        while len(q) > 0:
            current = q.dequeue()
            for n in current.neighbors:
                n.distance = current.distance + 1
                if n == node2:
                    return n.distance

                q.enqueue(n)

        return float('inf')

    def has_cycle(self):
        s = stack.Stack()
        for r in self.root_nodes:
            s.push(r)

        while len(s) > 0:
            current = s.pop()

            if current.color == "grey":
                if reduce(lambda x, y: x and y, map(lambda z: True if z == "black" else False, current.neighbors)):
                    current.color = "black"

                else:
                    return True

            elif current.color == "white":
                current.color = "grey"
                for n in current.neighbors:
                    s.push(n)

        self.reset()
        return False

    def reset(self):
        q = queue.Queue()
        for r in self.root_nodes:
            q.enqueue(r)

        while len(q) > 0:
            current = q.dequeue()

            current.color = "white"
            current.distance = 0

            for n in current.neighbors:
                q.enqueue(n)

        return None


class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.color = "white"
        self.distance = float('inf')

