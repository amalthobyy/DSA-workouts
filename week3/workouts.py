# class BST:
#     def __init__(self,key):
#         self.key=key
#         self.lchild=None
#         self.rchild=None
#     def insert(self,data):
#         if self.key is None:
#             self.key=data
#             return
#         if self.key==data:
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild=BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild=BST(data)
#     def preorder(self):
#         print(self.key,end=" ")
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.preorder()
#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key,end=" ")
#         if self.rchild:
#             self.rchild.inorder()
#     def postorder(self):
#         if self.lchild:
#             self.lchild.postorder()
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key,end=" ")                                
                    
                            
# root=BST(10)
# list1=[1,3,6,8,9,2,7]
# for i in list1:
#     root.insert(i)

print(root.inorder())
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    
    def count_nodes(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

   
    def validate_bst(self, node=None, min_value=float('-inf'), max_value=float('inf')):
        if node is None:
            node = self.root
        if not node:
            return True
        if not (min_value < node.value < max_value):
            return False
        return (self.validate_bst(node.left, min_value, node.value) and
                self.validate_bst(node.right, node.value, max_value))

   
    def is_identical(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.value == node2.value and
                self.is_identical(node1.left, node2.left) and
                self.is_identical(node1.right, node2.right))

    
    def height(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    
    def second_largest(self, node=None):
        if node is None:
            node = self.root
        prev, curr = None, node
        while curr.right:
            prev, curr = curr, curr.right
        if curr.left:
            return self._find_max(curr.left).value
        return prev.value

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node

    
    def kth_largest(self, k):
        self.k = k
        self.result = None
        self._reverse_inorder(self.root)
        return self.result

    def _reverse_inorder(self, node):
        if node and self.k > 0:
            self._reverse_inorder(node.right)
            self.k -= 1
            if self.k == 0:
                self.result = node.value
            self._reverse_inorder(node.left)

    def exists(self, value, node=None):
        if node is None:
            node = self.root
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.exists(value, node.left)
        else:
            return self.exists(value, node.right)


    def even_numbers(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return []
        result = []
        if node.value % 2 == 0:
            result.append(node.value)
        result.extend(self.even_numbers(node.left))
        result.extend(self.even_numbers(node.right))
        return result

    def is_subtree(self, main_tree, sub_tree):
        if not sub_tree:
            return True
        if not main_tree:
            return False
        if self.is_identical(main_tree, sub_tree):
            return True
        return (self.is_subtree(main_tree.left, sub_tree) or
                self.is_subtree(main_tree.right, sub_tree))


if __name__ == "__main__":
    bst = BST()

    
    for val in [15, 10, 20, 8, 12, 18, 25]:
        bst.insert(val)

    print("Total Nodes:", bst.count_nodes())  # 7
    print("Is Valid BST:", bst.validate_bst())  # True
    print("Height of BST:", bst.height())  # 3
    print("Second Largest:", bst.second_largest())  # 20
    print("3rd Largest:", bst.kth_largest(3))  # 18
    print("Element 12 Exists:", bst.exists(12))  # True
    print("Even Numbers in BST:", bst.even_numbers())  # [10, 8, 20, 12, 18]


    sub_bst = BST()
    for val in [10, 8, 12]:
        sub_bst.insert(val)
    print("Is Subtree:", bst.is_subtree(bst.root, sub_bst.root))  # True
