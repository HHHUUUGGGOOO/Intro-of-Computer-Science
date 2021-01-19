HEAPSIZE = 500000
class Node:
    def __init__(self):
        self.key = 0
        self.element = []

class Heap:
    def __init__(self):
        self.size=0
        self.ary=[ Node() for _ in range(HEAPSIZE)]

    def printArray(self):
        print("(Index, Key, Element)")
        for i in range(self.size):    #the length and order of index is equal to self.size
            print("({},{},{})".format(str(i),str((self.ary)[i].key),str((self.ary)[i].element)))

    def isempty(self):
        return ((self.size)==0)

    def printByPopping(self):
        while not (self.isempty()):
            print(self.pop(),end='')
        print("")

    def getTopKey(self):
        return (self.ary)[0].key

    def swap(self,i,j):
        (self.ary)[i], (self.ary)[j] = (self.ary)[j], (self.ary)[i] 
        
    def push(self,key,element):   #binary min heap
        now = self.size
        self.ary[now].key = key
        self.ary[now].element = element
        parent_index = (now-1)//2
        while self.ary[now].key < self.ary[parent_index].key:   #if the child < its parent, then swap them, repeat it until the child > its parent
            self.swap(now, parent_index)
            now = parent_index
            parent_index = (now-1)//2
        self.size += 1    
        
    def pop(self):
        self.size -= 1
        element = self.ary[0].element    #extract the root 
        self.ary[0], self.ary[self.size] = self.ary[self.size], Node()   #replace the last key to the root
        now = 0
        while True:
            left = 2*now + 1   #left child
            right = 2*now + 2    #right child
            if self.ary[now].key > self.ary[right].key and self.ary[left].key > self.ary[right].key and self.ary[right].key != 0:
                self.swap(now, right)   #search the min key and swap them, and we should ignore the zero
                now = right
            elif self.ary[now].key > self.ary[left].key and self.ary[right].key > self.ary[left].key and self.ary[left].key != 0:
                self.swap(now, left)
                now = left
            else:
                break
        return element
