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

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or None if not found
        Takes O(n) time
        """
        current = self.head

        while current != None:
            if current.data == key:
                return current
            current = current.next_node

        return None

    def insert(self, data, index):
        """
        Insert a new Node containing data at index position
        Insertion takes O(1) time but finding tje node at
        the insertion point takes O(n) time

        constant time operation
        Takes O(n) time 
        """
        if index == 0:
            self.add(data)
            
        if index > 0:
            new = Node(data)

            position = 0
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1
            
            prev = current
            next_node = current.next_node

            prev.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        remove node contaning data that matches the key
        Retuens the moce or None if key  doesn't exist
        Takes O(n) time

        linked is a good place to just study
        there's much more efficient method.
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            #key is head node (number that we want to remove is head)
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            #if current data is ket (number that we want to remove is this node)
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            #no data that matches the key
            else:
                previous = current
                current = current.next_node

        return current
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

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
        return "->".join(nodes)

    
"""
Prepend - data added to the head
Append - data added to the tail
"""