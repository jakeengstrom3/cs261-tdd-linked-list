# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:

    def __init__(self, value=None):
        
        self.value = value
        self.next = self
        self.prev = self

    def is_sentinel(self):
        return self.value is None

    def is_empty(self):
        return self.next is self and self.prev is self

    def is_last(self):
        return self.next.value is None

    def last(self):
        return self.prev

    def append(self, appendee):
        self.last().next = appendee #Sets the last elements next value to the appendee (was the sentinel)
        appendee.prev = self.last() #Sets the appendee's previous value to the recent last value 
        self.prev = appendee #Sets the sentinels previous to the new appendee
        appendee.next = self #Sets the appendees next value to the sentinel

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next = None
        self.prev = None

    def insert(self, insertee):
        self.next.prev = insertee
        insertee.prev = self
        insertee.next = self.next
        self.next = insertee

    def at(self, n):
        if(n == 0):
            return self
        return self.next.at(n - 1)

    def search(self, val):
        if(self.value == val):
            return self
        if self.next.is_sentinel():
            return None
        return self.next.search(val)

    def insert_in_order(self, node):

        if self.next.is_sentinel() or node.value < self.next.value:
            return self.insert(node)
        
        return self.next.insert_in_order(node)