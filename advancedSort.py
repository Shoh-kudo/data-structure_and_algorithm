
# coding: utf-8

# # マージソートはO(nlogn)
# ## 分割にO(logn), ソートにO(n)

# In[163]:


from collections import deque

def merge(L,R,cnt):
    L,R = deque(L),deque(R)
    A = [0]*(len(L)+len(R))
    for i in range(len(A)):
        if len(L) == 0:
            A[i] = R.popleft()
        elif len(R) == 0:
            A[i] = L.popleft()
        elif L[0] <= R[0]:
            A[i] = L.popleft()
        elif R[0] < L[0]:
            A[i] = R.popleft()
    return A

def mergeSort(A):
    if len(A) < 2:
        return A
    mid = (len(A))//2
    return merge(mergeSort(A[:mid]),mergeSort(A[mid:]))

def main():
    n = int(input())
    A = list(map(int,input().split()))
    
    A = mergeSort(A)
    print(' '.join(map(str,A)))
    
if __name__ == '__main__':
    main()


# # パーティション
# ## ある値を基準に代償を比較するだけならO(n)で十分

# In[296]:


def partition(A):
    q = A[-1]
    i = 0
    for j in range(len(A)):
        if A[j] < q:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[-1] = A[-1],A[i]
    return A,i

def main():
    n = int(input())
    A = list(map(int,input().split()))
    
    A,idx = partition(A)
    
    print(' '.join(map(str,A[:idx])),f'[{A[idx]}]', ' '.join(map(str,A[idx+1:])))
    
if __name__ == '__main__':
    main()


# # クイックソートは最も早いソートだが安定なソートではない

# In[303]:


def partition(A):
    q = A[-1]
    i = 0
    for j in range(len(A)):
        if A[j][1] < q[1]:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[-1] = A[-1],A[i]
    return A,i

def quickSort(A):
    if len(A) < 1:
        return A
    A,idx = partition(A)
    return quickSort(A[:idx])+[A[idx]]+quickSort(A[idx+1:])

def main():
    n = int(input())
    A = list()
    for i in range(n):
        a,b = input().split()
        A.append((a,int(b)))
    
    A = quickSort(A)
    for a in A:
        print(' '.join(map(str,a)))

if __name__ == '__main__':
    main()


# # 計数ソートは初めから配列を用意している分ソートは早いが
# # メモリを食う

# In[306]:


def countingSort(S):
    A,B,C = [0]*(len(S)+1),[0]*(len(S)+1),[0]*10000
    
    for num,s in enumerate(S):
        A[num] = s
        C[A[num]] += 1
    
    for c in range(1,len(C)):
        C[c] += C[c-1]
        
    for i in range(len(A)):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1
        
    return B

def main():
    n = int(input())
    S = list(map(int, input().split()))
    
    S = countingSort(S)
    
    print(' '.join(map(str,S[1:])))
    
if __name__ == '__main__':
    main()


# # 反点数
# ## バブルソートの交換回数と等しくなる

# In[319]:


from collections import deque

class InversionNumber(object):
    
    def __init__(self,A):
        self.cnt = 0
        self.A = A
        self.orderedA = self.mergeSort(self.A)
        
    def merge(self,L,R): #n
        L,R = deque(L),deque(R)
        A = [0]*(len(L)+len(R))
        
        for i in range(len(A)):
            if len(L) == 0:
                A[i] = R.popleft()
            elif len(R) == 0:
                A[i] = L.popleft()
            elif L[0] <= R[0]:
                A[i] = L.popleft()
            else:
                A[i] = R.popleft()
                self.cnt += len(L)
        return A
    
    def mergeSort(self,A): #logn
        if len(A) < 2:
            return A
        mid = (len(A))//2
        return self.merge(self.mergeSort(A[:mid]),self.mergeSort(A[mid:]))
    
def main():
    n = int(input())
    A = list(map(int,input().split()))
    
    inum = InversionNumber(A)
    print(inum.cnt)
    
if __name__ == '__main__':
    main()

