
# coding: utf-8

# In[1]:


#coding: utf-8


# # 線形探索はO(qn)の探索アルゴリズム

# In[7]:


def linearSearch(A,n,key):
    i = 0
    A[n] = key
    while A[i] != key:
        i += 1
    if i != n:
        return 1
    
def main():
    n = int(input())
    A = [0]*(n+1)
    A[:n] = map(int, input().split())
    
    q = int(input())
    B = list(map(int,input().split()))
    ans = 0
    for key in B:
        if linearSearch(A,n,key):
            ans += 1
        
    print(ans)
    
if __name__ == '__main__':
    main()


# # 二分探索はソート済みの配列を用いたO(n)の探索アルゴリズム

# In[37]:


def binarySearch(A,n,key):
    left = 0
    right = n
    while left < right:
        mid = (left+right)//2
        if A[mid] == key:
            return 1
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1

def main():
    n = int(input())
    A = list(map(int,input().split()))
    
    q = int(input())
    B = list(map(int,input().split()))
    ans = 0
    for key in B:
        if binarySearch(A,n,key):
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()


# # ハッシュ法はハッシュ関数というのを使うらしい．詳しくはわからん．

# In[49]:


class HashMethod(object):
    
    def __init__(self,M,H):
        self.M = M
        self.H = H
    
    def fromStrtoNum(self,char):
        if char == 'A': return 1
        elif char == 'C': return 2
        elif char == 'G': return 3
        elif char == 'T': return 4
        else: return 0
        
    def getKey(self,obj):
        key,p = 0, 1
        for i in obj:
            key += p * self.fromStrtoNum(i)
            p *= 5
        return key
    
    def hash1(self,key): #modをとるハッシュ関数1
        return key % self.M
    
    def hash2(self,key): #modをとるハッシュ関数2
        return 1 + (key % (self.M - 1))
    
    def find(self,obj):
        key = self.getKey(obj)
        count = 0
        while True:
            h = (self.hash1(key)+count*self.hash2(key)) % self.M
            if self.H[h] == key:
                return 1
            elif count >= self.M:
                return 0
            else:
                count += 1
        return 0
    
    def insert(self,obj):
        key = self.getKey(obj)
        count = 0
        while True:
            h = (self.hash1(key)+count*self.hash2(key)) % self.M
            if self.H[h] == None:
                self.H[h] = key
                return h
            else:
                count += 1
    
def main():
    M = int(input())
    H = [None]*M
    
    hm = HashMethod(M,H)
    
    for i in range(M):
        com, obj = input().split()
        
        if com[0] == 'i':
            hm.insert(obj)
        else:
            if hm.find(obj):
                print('yes')
            else:
                print('no')
    print(hm.H)
                
if __name__ == '__main__':
    main()


# # 最適解の計算を探索を用いて...

# In[62]:


class OptimTrack(object):
    
    def __init__(self,n,W,k):
        self.n = n
        self.W = W
        self.k = k
        
    def check(self,P):
        i = 0
        for j in range(self.k):
            s = 0
            while s + self.W[i] <= P:
                s += self.W[i]
                i += 1
                if i == self.n:
                    return self.n
        return i
    
    def solve(self):
        left = 0
        right = 100000 * 10000
        while right-left > 1:
            mid = (left+right)//2
            maxim = self.check(mid)
            if maxim >= self.n: #最大積載個数がnよりも大きいなら過剰に用意しすぎなので減らす方向に（最大値を下げる方向に）するために右端を削る
                right = mid
            else:
                left = mid
        return right
    
def main():
    n,k = map(int,input().split())
    W = [0]*n
    for i in range(n):
        W[i] = int(input())
    
    ot = OptimTrack(n,W,k)
    
    ans = ot.solve()
    
    print(ans)
    
if __name__ == '__main__':
    main()

