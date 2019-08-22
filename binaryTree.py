
# coding: utf-8

# # 二分探索木

# In[30]:


class Node(object):
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.null = None
        self.order = []
        
    def insert(self,key):
        x = self.root
        node = Node(key)
        y = node.left = node.right = self.null
        
        while x != None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.null:
            self.root = node
        else:
            if node.key < y.key:
                y.left = node
            else:
                y.right = node
                
    def inorder(self,u):
        if not u:
            return
        self.inorder(u.left)
        self.order += [u.key]
        self.inorder(u.right)
            
    def preorder(self,u):
        if not u:
            return
        self.order += [u.key]
        self.preorder(u.left)
        self.preorder(u.right)
        
    def init_order(self):
        self.order = []
        
def main():
    n = int(input())
    bt = BinaryTree()
    
    for i in range(n):
        com = input()
        
        if com[0] == 'i':
            command,num = com.split()
            bt.insert(int(num))
        
        if com[0] == 'p':
            bt.inorder(bt.root);print(' '.join(map(str,bt.order)))
            bt.init_order()
            bt.preorder(bt.root);print(' '.join(map(str,bt.order)))
            
if __name__ == '__main__':
    main()


# In[34]:


class Node(object):
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.null = None
        self.order = []
        
    def insert(self,key):
        x = self.root
        node = Node(key)
        y = node.left = node.right = None
        
        while x != self.null:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.null:
            self.root = node
        else:
            if node.key < y.key:
                y.left = node
            else:
                y.right = node
    
    def find(self,key):
        x = self.root
        while x != self.null and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def preorder(self,u):
        if u == self.null:
            return
        self.order += [u.key]
        self.preorder(u.left)
        self.preorder(u.right)
        
    def inorder(self,u):
        if u == self.null:
            return
        self.inorder(u.left)
        self.order += [u.key]
        self.inorder(u.right)
        
    def init_order(self):
        self.order = []
        
def main():
    n = int(input())
    bt = BinaryTree()
    
    for i in range(n):
        command = input()
        
        if command[0] == 'i':
            com,num = command.split()
            bt.insert(int(num))
            
        if command[0] == 'p':
            bt.inorder(bt.root);print(' '.join(map(str,bt.order)))
            bt.init_order()
            bt.preorder(bt.root);print(' '.join(map(str,bt.order)))
            bt.init_order()
            
        if command[0] == 'f':
            com,num = command.split()
            if bt.find(int(num)):
                print('yes')
            else:
                print('no')
                
if __name__ == '__main__':
    main()


# In[39]:


class Node(object):
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.order = []
        self.positon = None
        
    def insert(self,key):
        x = self.root
        node = Node(key)
        y = node.left = node.right = None
        
        while x != None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        else:
            if node.key < y.key:
                y.left = node
            else:
                y.right = node
    
    def find(self,key):
        x = self.root
        while x != None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def treeMinimum(self,node):
        while node.left != None:
            node = node.left
        return node
    
    def getNextNode(self,node):
        if node.right != None:
            return self.treeMinimum(node)
        y = node.parent
        while y != None and node == y.right:
            x = y
            y = y.parent
        return y
    
    def delete(self,key):
        z = self.find(key)
        if z.left == None or z.right == None:
            y = z
        else:
            y = self.getNextNode(z)
            
        if y.left != None:
            x = y.left
        else:
            x = y.right
        if x != None:
            x.parent = y.parent
        if y.parent == None:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        if y != z:
            z.key = y.key
      
    def preorder(self,u):
        if u == None:
            return
        self.order += [u.key]
        self.preorder(u.left)
        self.preorder(u.right)
        
    def inorder(self,u):
        if u == None:
            return
        self.inorder(u.left)
        self.order += [u.key]
        self.inorder(u.right)
        
    def init_order(self):
        self.order = []
    
def main():
    n = int(input())
    bt = BinaryTree()
    
    for i in range(n):
        command = input()
        
        if command[0] == 'i':
            com,num = command.split()
            bt.insert(int(num))
            
        if command[0] == 'p':
            bt.inorder(bt.root);print(' '.join(map(str,bt.order)))
            bt.init_order()
            bt.preorder(bt.root);print(' '.join(map(str,bt.order)))
            bt.init_order()
            
        if command[0] == 'f':
            com,num = command.split()
            if bt.find(int(num)):
                print('yes')
            else:
                print('no')
                
        if command[0] == 'd':
            com,num = command.split()
            bt.delete(int(num))
                
if __name__ == '__main__':
    main()


# In[ ]:


# 

