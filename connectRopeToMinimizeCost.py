"""In this problem we've given a array containing len of a rope and we need to connect the ropes to minimize
the cost"""

import heapq
def ropeCost(arr):
    heapq.heapify(arr)
    sum=0
    while(len(arr)>1):
        val1=heapq.heappop(arr)
        val2=heapq.heappop(arr)
        #we take two minimum number from a array
        data1=val1+val2
        sum=sum+data1
        #we again push the sum of two smallest element in the array
        heapq.heappush(arr,data1)
    return sum

arr=[1,2,3,4,5]
print(ropeCost(arr))
