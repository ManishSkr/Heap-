"""here we need to find k number of closest element of a given number in the arr, This problem is also a 
variation of heap"""

import heapq

def kClosest(arr,k,x):
    pair=[(abs(i-x),i)for i in arr]

    heapq.heapify(pair)
    val=heapq.nsmallest(k,pair)

    return [x[1] for x in val]

arr=[5,6,7,8,9]

k=3
x=7
#here we find k no element which is closest to x
print(kClosest(arr,k,x))