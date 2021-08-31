"""This question is also known as nearly sorted array"""
import heapq

def ksorted(arr,k):
    heapq.heapify(arr)
    sort=[]
    while(arr):
        heapq.nsmallest(3,arr)
        sort.append(heapq.heappop(arr))
    return sort

arr=[6,5,3,2,8,10,9]
k=3

print(ksorted(arr,k))