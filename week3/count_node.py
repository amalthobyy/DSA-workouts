class BST:
    def __init__(self,key):
        self.key=key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if data==self.key:
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild =BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def count_nodes(self):
        if self.key is None:
            return 0
        left_count = self.lchild.count_nodes() if self.lchild else 0
        right_count = self.rchild.count_nodes() if self.rchild else 0
        return 1 + left_count + right_count
def targetexists(root,target):
        if not root:
            return False
        if root.key ==target:
            return True
        if target< root.key:
            return targetexists(root.lchild,target)
        return targetexists(root.rchild,target)
    


root = BST(10)
list1 = [8, 9, 5, 4, 3, 2]
for i in list1:
    root.insert(i)
target=12
print("Target exists:", targetexists(root, target))