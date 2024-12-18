# graph={}
# def add_node(v):
#     if v in graph:
#         print(v,"in graph")
#     else:
#         graph[v]=[]
# def add_edge(v1,v2):
#     if v1 in graph:
#         print(v1,"in graph")
#     elif v2 not in graph:
#         print(v2,"not in graph")
#     else:
#         graph[v1].append(v2)
# def dfs(graph,node,visited=set()):
#     if node not in visited:
#         print (node,end=" ")
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs(graph,neighbor,visited)

# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# add_node("e")
# print(graph)
# dfs(graph,"a")
# print()

class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def validate(root,min=float("-inf"),max=float("inf")):
        if not root:
            return True
        if not(min<root.key<max):
            return False
        return True 

root=BST(10)
list1=[1,3,5,2,7,9]
for i in list1:
    root.insert(i)
print(root.validate())         
