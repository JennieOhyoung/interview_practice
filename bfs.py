"""
Tree traversal. BFS and DFS (pre, in, post)
"""

class BinaryTree:
    def __init__(self,data):
        self.key = data
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def bfs(tree):
    l = [tree.key]
    while l:
        node = l.pop[0]
        if node.getLeftChild:
            l.append(node.getLeftChild().getRootVal())
        if node.getRightChild:
            l.append(node.getRightChild().getRootVal())


def bfs(tree):


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getLeftChild().insertLeft('d')
r.getLeftChild().insertRight('e')
r.getRightChild().insertLeft('f')
r.getRightChild().insertRight('g')
# print r.getLeftChild().getRootVal()
print r.key


print bfs(r)















