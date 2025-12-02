# QUEUE IMPLEMENTATION FOR ORDER PROCESSING (FIFO)

class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        self.queue.append(order)

    def process_order(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def get_orders(self):
        return self.queue
