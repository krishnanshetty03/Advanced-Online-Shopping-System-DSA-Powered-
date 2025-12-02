# LINKED LIST CART IMPLEMENTATION

class Node:
    def __init__(self, product):
        self.product = product
        self.next = None

class LinkedListCart:
    def __init__(self):
        self.head = None

    def add(self, product):
        new_node = Node(product)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def remove(self, product_id):
        temp = self.head
        prev = None
        while temp:
            if temp.product["id"] == product_id:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return temp.product
            prev = temp
            temp = temp.next
        return None

    def get_all(self):
        items = []
        temp = self.head
        while temp:
            items.append(temp.product)
            temp = temp.next
        return items
