#!/usr/bin/python3
"""class Node that defines a node of a singly linked list by:

    Private instance attribute: data:
    property def data(self): to retrieve it
    property setter def data(self, value): to set it:
        data must be an integer, otherwise raise a TypeError exception with
        the message data must be an integer
        Private instance attribute: next_node:
            property def next_node(self): to retrieve it
            property setter def next_node(self, value): to set it:
                next_node can be None or must be a Node, otherwise raise a
                TypeError exception with the message next_node must be a
                Node object
                Instantiation with data and next_node: def __init__(self,
                data, next_node=Node)
"""


class Node:

    def __init__(self, data, next_node=None):
        """Initializes the data of the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data into a node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Private instance attribute: head (no setter or getter)
Simple instantiation: def __init__(self):
    Should be printable:
        print the entire list in stdout
        one node number by line
        Public instance method: def sorted_insert(self, value):
        that inserts a new Node into the correct sorted position in the list
        (increasing order)
"""


class SinglyLinkedList:
    """ Singly linked list.
    Private instance attribute: head.
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """

    def __init__(self):
        """Initializes the linked list."""
        self.head = None

    def __str__(self):
        """For the print statement in the main file."""
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_nod
