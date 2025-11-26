class Node:
    def __init__(self, key, value):
        self.key: int = key
        self.value: int = value
        self.left: Node = None
        self.right: Node = None

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.insert(key, value)


    def search(self, key):
        if self is None: return None
        if self.key == key: return self
        return self.left.search(key) if key < self.key else self.right.search(key)

    def get_min(self):
        if self is None: return None
        if self.left is None: return self
        return self.left.get_min()

    def get_max(self):
        if self is None: return None
        if self.right is None: return self
        return self.right.get_max()

root = Node(5, 100)

root.insert(1, 20)
root.insert(4, 30)
root.insert(6, 30)

print(root.right.key, ":", root.right.value)

print(root.get_max().key)