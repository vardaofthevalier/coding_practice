from linked_list import SinglyLinkedList


class AdjacencyListGraph(object):
    def __init__(self):
        # the inner adjacency list contains linked lists of tuples, where each tuple contains the index of a node and the edge weight between the two nodes
        self.adjacency_list = []