# TREE STRUCTURE FOR PRODUCT CATEGORY BROWSER

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def build_category_tree():
    root = TreeNode("Store")

    electronics = TreeNode("Electronics")
    accessories = TreeNode("Accessories")
    mobile = TreeNode("Mobiles")

    electronics.add_child(TreeNode("Laptops"))
    electronics.add_child(TreeNode("Audio Devices"))

    accessories.add_child(TreeNode("Cables"))
    accessories.add_child(TreeNode("Computer Accessories"))

    mobile.add_child(TreeNode("Smartphones"))
    mobile.add_child(TreeNode("Chargers"))

    root.add_child(electronics)
    root.add_child(accessories)
    root.add_child(mobile)

    return root
