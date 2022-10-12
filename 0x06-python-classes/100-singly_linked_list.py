#!/usr/bin/python3
"""Define a class Square."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and value:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        headn = self.__head
        new = Node(value)

        if not headn:
            self.__head = new
        elif headn.data >= value:
            new.next_node = headn
            self.__head = new
        else:
            prevn = self.__head
            while headn:
                if headn.data >= value:
                    new.next_node = headn
                    prevn.next_node = new
                    return

                prevn = headn
                headn = headn.next_node
            prevn.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        string = []
        headn = self.__head

        while headn:
            string.append(str(headn.data))
            headn = headn.next_node

        return ('\n'.join(string))
