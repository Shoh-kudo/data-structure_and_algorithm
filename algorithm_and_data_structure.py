
# coding: utf-8

# In[90]:


import numpy as np


# In[10]:


n = int(input())
A = list(map(int, input().split()))
ans = []

for num in range(n):
    ans.append(max(A))
    A.remove(max(A))
    
print(ans)


# In[12]:


n = int(input())
A = list(map(int, input().split()))
A.sort()
ans = []

for num in range(n):
    ans.append(A.pop())
    
print(ans)


# In[40]:


# O(n)

n = int(input())
minimum_value = 1e10
max_diff = -1e10

for num in range(n):
    current_value = int(input())

    current_diff = current_value - minimum_value
    max_diff = max([current_diff,max_diff])
    minimum_value = min([current_value,minimum_value])

print(max_diff)


# In[36]:


#　O(n^2)　あくまでオーダーなので厳密にn^2時間かかっているわけではない

maxv = -1e10

n = int(input())
R = list(int(input()) for n in range(n))

for j in range(0, n):
    for i in range(0, j):
        maxv = max([maxv, R[j]-R[i]])
        
print(maxv)


# In[50]:


# O(n^2) 最悪で(n^2-n)/2

def insertionSort(N,A):
    for i in range(N):
        v = A[i] #一時的に保存
        j = i-1 #i番目の一個手前までをサーチ
        while j >= 0 and A[j] > v: #未ソート部分がなくなるまで
            A[j+1] = A[j] #自分の方が小さければ挿入
            j -= 1
            A[j+1] = v #挿入してなくなった部分を返す
        print(' '.join(map(str,A)))

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    insertionSort(N,A)

if __name__ == '__main__':
    main()


# In[61]:


# O(n^2) 最悪で(n^2-n)/2

def bubbleSort(N,A):
    flag = 1
    i = 0
    count = 0
    while flag:
        flag = 0
        for j in range(N-1,i,-1): #N-1番目から(リストの最後)
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1 #一度でも交換があればflagたつ
                count+=1 #交換回数をカウント
        i += 1
    print(' '.join(map(str,A)))
    print(count)
                
def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    bubbleSort(N,A)
    
if __name__ == '__main__':
    main()


# In[67]:


# 常にO(n^2)のソートかつ不安定なソート

def selectionSort(A,N) -> None:
    
    count = 0
    for i in range(N-1): #最後までいけばすでにソートされているので
        minimum_num = i
        for j in range(i,N):
            if A[minimum_num] > A[j]:
                minimum_num = j
        if i != minimum_num:
            A[i], A[minimum_num] = A[minimum_num], A[i]
            count += 1
            print(' '.join(map(str,A)))
    print(count)
        
def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    selectionSort(A,N)
    
if __name__ == '__main__':
    main()


# In[ ]:


N = int(input())
A = list(map())


# In[89]:


def bubbleSort(N,A) -> list:
    flag = 1
    i = 0
    while flag:
        flag = 0
        for j in range(N-1,i,-1):
            if A[j][1] < A[j-1][1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
        i += 1
    return [''.join(map(str,a)) for a in A]

def selectionSort(N,A) -> list:
    for i in range(N-1):
        minimum_num = i
        for j in range(i,N):
            if A[minimum_num][1] > A[j][1]:
                minimum_num = j
        if i != minimum_num:
            A[i], A[minimum_num] = A[minimum_num], A[i]
    return [''.join(map(str,a)) for a in A]

def judgeStable(bubbleA, selectionA) -> None:
    if bubbleA == selectionA:
        bubbleA, selectionA = ' '.join(bubbleA), ' '.join(selectionA)
        print(f'{bubbleA}\nStable\n{selectionA}\nStable')
    else:
        bubbleA, selectionA = ' '.join(bubbleA), ' '.join(selectionA)
        print(f'{bubbleA}\nStable\n{selectionA}\nNot stable')

def main() -> None:
    N = int(input())
    A = [(a[0],int(a[1])) for a in list(input().split())]
    
    bubbleA = bubbleSort(N,A)
    selectionA = selectionSort(N,A)

    judgeStable(bubbleA, selectionA)
    
if __name__ == '__main__':
    main()


# In[102]:


#shell sort は挿入ソートの改良したもの．

def insertionSort(A,n,g,cnt):
    for i in range(g,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return A,cnt

def shellSort(A,n):
    G = []
    cnt = 0
    for h in range(5):
        G.append(3*h+1)
    G_print = G.copy()
    while G:
        g = G.pop()
        A,cnt = insertionSort(A,n,g,cnt)
    return A, len(G_print), G_print

def main():
    n = int(input())
    A = []
    
    for i in range(n):
        A.append(int(input()))
        
    A,len_g,G = shellSort(A,n)
    print(f'{len_g}')
    G = [G.pop() for i in range(len_g)]
    print(" ".join(map(str,G)))
    for a in A:
        print(a)
        
if __name__ == '__main__':
    main()


# In[143]:


# 逆ポーランド記法

from collections import deque

class StackStructure(object):
    
    def __init__(self):
        self.top = 0
        self.S = [0]*100 #最大100までスタックできる
        
    def push(self,x):
        self.top += 1
        self.S[self.top] = x
        
    def pop(self):
        self.top -= 1
        return self.S[self.top+1]
    
def operation(a,b,x):
    if x == '+':
        return a+b
    elif x == '-':
        return a-b
    elif x == '*':
        return a*b

def main():
    SS = StackStructure()
    s = deque(input().split())
    
    while s:
        x = s.popleft()
        try:
            SS.push(int(x)) #処理の順番はxのint化->SS.push
        except:
            a = SS.pop() #topからpop
            b = SS.pop() #topからpop
            SS.push(operation(b,a,x)) #演算は下にあるものを先にかくのでb*a
        
    print(SS.S[1])
    
if __name__ == '__main__':
    main()


# In[165]:


#ラウンドロビンスケジューリング，リングバッファ

from collections import deque

class QueStructure(object):
    
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.S = [0]*100005
        self.len = len(self.S)
        
    def enqueue(self,x):
        self.S[self.head] = x
        self.head = (self.head+1)%self.len
        
    def dequeue(self):
        self.tail = (self.tail+1)%self.len
        return self.S[self.tail-1]
        
def main():
    n, q = map(int, input().split())
    name = QueStructure()
    time = QueStructure()
    
    for i in range(n):
        name_i, time_i = (input().split())
        name.enqueue(name_i)
        time.enqueue(int(time_i))
    
    elaps = 0
    while time.head != time.tail:
        u_name, u_time = name.dequeue(), time.dequeue()
        c = min([q, u_time])
        u_time -= c
        elaps += c
        if u_time > 0:
            time.enqueue(u_time)
            name.enqueue(u_name)
        else:
            print(f'{u_name} {elaps}')
        
if __name__ == '__main__':
    main()


# In[199]:


#python verのdoubly linked list

import gc

class Node(object):
    
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None
        
class DoublyLinkedList(object):
    
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil
        
    def insert(self, x):
        new = Node(x) #新しいノードを作成
        new.next = self.nil.next #全体の末端を更新
        self.nil.next.prev = new #末端の直前を更新
        self.nil.next = new #先端の次点を更新
        new.prev = self.nil #新規ノードの先端を先端に接続
        
    def listSearch(self, x):
        cur = self.nil.next #先端の次点から開始
        while cur != self.nil and cur.key != x: #nilに当たらないかつkeyがxでない限り続ける
            cur = cur.next #curを次に更新する
        return cur
    
    def deleteNode(self, t):
        if t == self.nil: #tが初期値にある場合を考慮
            return
        t.prev.next = t.next #tの一個前に戻ってtをtの一個後のものに更新
        t.next.prev = t.prev #tの一個後に行ってtをtの一個前のものに更新
        gc.collect()
        
    def deleteFirst(self):
        self.deleteNode(self.nil.next)
        
    def deleteLast(self):
        self.deleteNode(self.nil.prev)
        
    def deleteKey(self, x):
        self.deleteNode(self.listSearch(x)) #サーチしたNodeを消去
        
    def printList(self):
        cur = self.nil.next
        ans = []
        while True:
            if cur == self.nil:
                break
            ans.append(cur.key)
            cur = cur.next
        print(' '.join(map(str,ans)))

def main():
    dll = DoublyLinkedList()
    n = int(input())
    for i in range(n):
        com, key = input().split()
        if com[0] == 'i':
            dll.insert(int(key))
        elif com[0] == 'd':
            if len(com) > 6:
                if com[6] == 'F':
                    dll.deleteFirst()
                elif com[6] == 'L':
                    dll.deleteLast()
            else:
                dll.deleteKey(int(key))
    dll.printList()
    
if __name__ == '__main__':
    main()

