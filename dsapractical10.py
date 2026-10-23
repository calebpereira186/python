class node(self,value):
    self.left = None
    self.right = None
    self.value = value
class binarytree:
    def __init__(self):
        self.root = None
    def inorder_traversal(self, start,traversal):
        if start:
            self.inorder_traversal(start.left,traversal)
            traversal+= (str(start.value) + '-')
            traversal+= self.inorder_traversal(start.right,traversal)
        return traversal
    def preorder_traversal(self, start,traversal):
        if start:
            traversal+= (str(start.value) + '-')
            traversal+= self.preorder_traversal(start.left,traversal)
            traversal+= self.preorder_traversal(start.right,traversal)
        return traversal
    def postorder_traversal(self, start,traversal):
        if start:
            traversal+= self.postorder_traversal(start.left,traversal)
            traversal+= self.postorder_traversal(start.right,traversal)
            traversal+= (str(start.value) + '-')
        return traversal
tree = binarytree()
tree.root.left = node(1)
tree.root.right = node(2)
tree.root.left.left = node(3)
tree.root.left.right = node(4)
print(tree.inorder_traversal(tree.root,''))
print(tree.preorder_traversal(tree.root,''))
print(tree.postorder_traversal(tree.root,''))
