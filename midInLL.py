"""Find the middle item in a singly linked list or two middle items
    if it contains an even number of nodes.

    input: linkedlist
    output: the data(datas) in middle

    len of linkedlist, find mid , mid+1
    loop and keep track of count. if count is equal to mid and return data,
    if it’s mid-1, return data, mid, return data

    Node cls = data,  next
    linkedlist cls = head, tail
"""



class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)
# node = Node(1)
# print("node: ", node)

class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: O(n) under what conditions? we have to
        traverse through the linkedlist to increment the node count by one until
        we reach to null"""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count


    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) under what conditions?
        since we have access to the tail node we don't have to traverse
        through the linked list to get to the last node"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            new_node.prev = None
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            new_node.prev = self.tail
            self.tail.next = new_node
        # Update tail to new node regardless
        # print("prev", new_node.prev, "item", item)
        self.tail = new_node
        self.size += 1

ll = LinkedList([1, 2, 3, 4, 5])
# print("ll: ", ll)

def middleitem(ll):
    """ Running-Time: O(n)
        Space: O(1) if len of ll is odd or O(2) if len of ll is even
    """
    print("ll: ", ll)
    mid = ll.length()//2
    cur_node = ll.head #starting head
    count = 0
    midEle = []
    while count < mid:
        if ll.length() % 2 == 0 and count + 1 == mid:
            midEle.append(cur_node.data)
        cur_node = cur_node.next
        count +=1
    midEle.append(cur_node.data)
    return midEle

print("result", middleitem(ll))
