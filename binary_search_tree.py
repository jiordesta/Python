class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left  = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
                else:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
    def search(self,value):
        current_node = self.root
        while True:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value > current_node.value:
                current_node = current_node.left
            else:
                return None
bst = BinarySearchTree()
for val in [3,54,6,8,9,0,1,2,44,45,66,77,76,42,12]:
    bst.insert(val)
print(bst.search(54))