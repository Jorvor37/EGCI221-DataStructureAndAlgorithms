#Self Referential Objects, Tail have no pointer to other nodes
class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    #run in linear time
    def size(self):
        """
        Return the number of nodes in the list
        runs in linear time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Add new Node containing data at head of the list
        Takes O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node == None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

    
"""
Prepend - data added to the head
Append - data added to the tail
"""