class Queue(object):
    """Creates a Queue, that can add elements to a queue, and they maintain a specific order.
    When you want to get something off the end of a queue, you get the
    item that has been in there the longest."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        self.vals.append(e)

    def remove(self):
        '''Removes an element from the attribute list'''
        # Check if the list is empty; if so then raise a ValueError
        if self.vals == []:
            raise ValueError()
        else:
            # Otherwise we want to remove the first element from the list
            # and return that to the user.
            firstElement = self.vals[0]
            self.vals.remove(firstElement)
            return firstElement
            # Could also do this in 1 line:
            # return self.vals.pop(0)