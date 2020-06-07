


class Stack(object):

    def __init__(self):
        self.items = ['x','y']

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def length(self):
        return len(self.items)