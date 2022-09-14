#!/usr/bin/python3
"""module containing class for a node of a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if(not(isinstance(value, int))):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if(not(isinstance(value, Node)) and not(value is None)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """single linked list class, with method to add new node
    in increasing order, and string representaion of node values
    of each node on a single line"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if(self.__head is None):
            new_node.next_node = None
            self.__head = new_node
            return
        else:
            prev_node = None
            current = self.__head
            while(current is not None):
                if(current.data >= new_node.data):
                    if(prev_node is None):
                        new_node.next_node = current
                        self.__head = new_node
                        return
                    else:
                        prev_node.next_node = new_node
                        new_node.next_node = current
                        return
                prev_node = current
                current = current.next_node
            new_node.next_node = None
            prev_node.next_node = new_node
            return

    def __str__(self):
        result = ""
        if(self.__head is not None):
            current = self.__head
            while(current is not None):
                result += str(current.data)
                current = current.next_node
                if(current is not None):
                    result += "\n"
        return result
