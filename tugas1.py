class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = max(
            self.height(y.left),
            self.height(y.right)
        ) + 1

        x.height = max(
            self.height(x.left),
            self.height(x.right)
        ) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = max(
            self.height(x.left),
            self.height(x.right)
        ) + 1

        y.height = max(
            self.height(y.left),
            self.height(y.right)
        ) + 1

        return y

    def insert(self, root, key):

        if root is None:
            return AVLNode(key)

        if key < root.data:
            root.left = self.insert(root.left, key)

        elif key > root.data:
            root.right = self.insert(root.right, key)

        else:
            return root

        root.height = max(
            self.height(root.left),
            self.height(root.right)
        ) + 1

        balance = self.balance_factor(root)

        
        if balance > 1 and key < root.left.data:
            return self.right_rotate(root)

        
        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)

        
        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        
        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)



avl = AVLTree()
root = None

data = [30, 20, 40, 10, 25, 35]

for x in data:
    root = avl.insert(root, x)

print("Inorder Traversal:")
avl.inorder(root)