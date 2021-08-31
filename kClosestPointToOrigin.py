"""Here we've given an array 1D or 2D and we need to find k no of points which is closest to origin"""

import heapq
def kClosestPoint(arr,k):
    heap=[]
    for row in arr:
        heap.append((row[0]**2+row[1]**2,(row[0],row[1])))
    heapq.heapify(heap)
    val=heapq.nsmallest(k,heap)
    return [x[1] for x in val]

arr=[[1,3],
     [-2,2],
     [5,8],
     [0,1]]
k=2
print(kClosestPoint(arr,k))