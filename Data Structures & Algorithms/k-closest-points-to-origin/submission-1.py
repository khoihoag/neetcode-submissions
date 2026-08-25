import math

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

        if left < n and self.arr[smallest][1] > self.arr[left][1]:
            smallest = left
        if right < n and self.arr[smallest][1] > self.arr[right][1]:
            smallest = right
        
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]

            self.sift_down(smallest, n)
    
    def extract_min(self):
        if len(self.arr) > 1:
            ans = self.arr[0]
            self.arr[0] = self.arr.pop()
            self.sift_down(0, len(self.arr))
            return ans
        elif len(self.arr) == 1:
            return self.arr.pop()

class Solution:
    def kClosest(self, points, k):
        res = [(i, math.sqrt(j[0]*j[0] + j[1]*j[1])) for i, j in enumerate(points)]
        heap = Heap(res) 
        ans = [points[heap.extract_min()[0]] for _ in range(k)]
        return ans