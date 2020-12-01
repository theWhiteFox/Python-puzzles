"""The LinkedList code from before is provided below. 
Add three functions to the LinkedList.
"get_position" returns the element at a certain position 
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
                
    def get_position(self, position):
        """Get an element form a particular postion.
        Assume the first position is "1".
        Ruturn "None if the position is not on the list."""
        print position = LinkedList.self
        if Element.position:
            print Element.position
        else:
            return None
    
    def insert(self, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        inserting at position 3 means between
        the 2nd and 3rd elements."""
        pass


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append = LinkedList(e2)
ll.append = LinkedList(e3)

https: // stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/
https: // developers.google.com/edu/python/lists
# print ll.head.next.next.value
# print ll.get_position(3).value
