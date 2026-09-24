class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.heapify()

    def heapify(self):
        for i in range(len(self.arr)//2-1, -1, -1):
            self.sift_down(i, len(self.arr))

    def sift_down(self, i, n):
        smallest = i
        left = i*2+1
        right = i*2+2

        if left < n and self.arr[smallest] > self.arr[left]:
            smallest = left
        if right < n and self.arr[smallest] > self.arr[right]:
            smallest = right
        
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]

            self.sift_down(smallest, n)
    
    def sift_up(self, i):
        while i > 0:
            parent = (i-1)//2

            if self.arr[i] < self.arr[parent]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break

    def add(self, value):
        self.arr.append(value)
        self.sift_up(len(self.arr)-1)

    def pop(self):
        self.arr[0] = self.arr.pop()
        self.sift_down(0, len(self.arr))
        
class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.heap = Heap(nums)

        while len(self.heap.arr) > k:
            self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.add(val)
        if len(self.heap.arr) > self.k:
            self.heap.pop()
        
        return self.heap.arr[0]