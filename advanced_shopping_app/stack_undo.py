# STACK USED FOR UNDO REMOVAL FROM CART

class UndoStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)
