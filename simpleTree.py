
# coding: utf-8

# # 根付き木

# In[57]:


class RootedTree(object):
    
    def __init__(self,n):
        self.tree = [None]*n
        self.depth = [0]*n
        self.parent = [-1]*n
        self.position = [None]*n
        
    def insert(self,number,num_of_child,child):
        self.tree[number] = child
        for n in self.tree[number]:
            self.parent[n] = number
            self.depth[n] += self.depth[self.parent[n]]+1
        if self.parent[number] == -1:
            self.position[number] = 'root'
        elif num_of_child == 0:
            self.position[number] = 'leaf'
        else:
            self.position[number] = 'internal node'
            
def main():
    n = int(input())
    rt = RootedTree(n)
    
    for node in range(n):
        number,num_of_child,*child = map(int,input().split())
        rt.insert(number,num_of_child,child)

        print(f'node {node}: parent = {rt.parent[node]}, depth {rt.depth[node]}, {rt.position[node]}, {rt.tree[node]}')
    
if __name__ == '__main__':
    main()


# # 二分木

# In[240]:


class Node(object):
    
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree(object):
    
    def __init__(self,n):
        self.D = [0]*(n+1)
        self.T = [None]*(n+1)
        self.H = [0]*(n+1)
        for t in range(n+1):
            self.T[t] = Node(-1,-1,-1) #[Node(-1,-1,-1)]*nにすると，全てが連動して動くのでだめ．for文回してこ．
    
    def insert(self,idx,left,right):
        self.T[idx].left,self.T[idx].right = left,right
        self.T[left].parent,self.T[right].parent = idx,idx
    
    def setDepth(self,u,d):
        if u == -1:
            return
        self.D[u] = d
        self.setDepth(self.T[u].left,d+1)
        self.setDepth(self.T[u].right,d+1)
        
    def setHeight(self,u):
        h1,h2 = 0,0
        if self.T[u].left != -1:
            h1 = self.setHeight(self.T[u].left)+1
        if self.T[u].right != -1:
            h2 = self.setHeight(self.T[u].right)+1
        self.H[u] = max([h1,h2])
        return self.H[u]
    
    def getSibling(self,u):
        if self.T[u].parent == -1:
            return -1
        if self.T[self.T[u].parent].left != -1 and self.T[self.T[u].parent].left != u:
            return self.T[self.T[u].parent].left
        if self.T[self.T[u].parent].right != -1 and self.T[self.T[u].parent].right != u:
            return self.T[self.T[u].parent].right
        return -1
    
    def getDegree(self,u):
        deg = 0
        if self.T[u].left != -1:
            deg += 1
        if self.T[u].right != -1:
            deg += 1
        return deg
    
    def getType(self,u):
        if self.T[u].parent == -1:
            return 'root'
        elif self.T[u].left == self.T[u].right == -1:
            return 'leaf'
        else:
            return 'internal node'
    
def main():
    n = int(input())
    bt = BinaryTree(n)
    
    for i in range(n):
        idx,left,right = map(int,input().split())
        bt.insert(idx,left,right)
        
    bt.setDepth(0,0),bt.setHeight(0)
    
    for i in range(n):
        print(f'node {i}: parent = {bt.T[i].parent}, sibling = {bt.getSibling(i)}, degree = {bt.getDegree(i)}, depth = {bt.D[i]}, height = {bt.H[i]}, {bt.getType(i)}')
        
if __name__ == '__main__':
    main()


# In[327]:


class Node(object):
    
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        
class BinaryTreeWalk(object):
    
    def __init__(self,n):
        self.n = n
        self.tree = [None]*(n+1)
        for i in range(n+1):
            self.tree[i] = Node()
        self.order = []
        
    def init_order(self):
        self.order = []
            
    def insert(self,idx,left,right):
        self.tree[idx].left,self.tree[idx].right = left,right
        self.tree[left].parent = self.tree[right].parent = idx
        
    def preorder(self,idx=0):
        if idx == -1:
            return
        self.order += [idx]
        self.preorder(self.tree[idx].left)
        self.preorder(self.tree[idx].right)
    
    def inorder(self,idx=0):
        if idx == -1:
            return
        self.inorder(self.tree[idx].left)
        self.order += [idx]
        self.inorder(self.tree[idx].right)
                
    def postorder(self,idx=0):
        if idx == -1:
            return
        self.postorder(self.tree[idx].left)
        self.postorder(self.tree[idx].right)
        self.order += [idx]
        
    def ans(self):
        
        self.preorder()
        a = " ".join(map(str,self.order))
        
        self.init_order(); self.inorder()
        b = " ".join(map(str,self.order))
        
        self.init_order(); self.postorder()
        c = " ".join(map(str,self.order))
        
        print(f'Preorder\n {a}\nInorder\n {b}\nPostorder\n {c}')
        
def main():
    n = int(input())
    
    bt = BinaryTreeWalk(n)
    for i in range(n):
        idx,left,right = map(int,input().split())
        bt.insert(idx,left,right)
    
    bt.ans()
    
if __name__ == '__main__':
    main()

