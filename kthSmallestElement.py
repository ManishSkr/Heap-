"""This is the variation of heap where we find the  kth smallest element"""
import heapq
def kSmallest(arr,k):
    heapq.heapify(arr)
    return heapq.nsmallest(k,arr)

arr=[7,10,4,3,20,15]
k=3
print("The kth largest element is ",end="")
print(kSmallest(arr,k)[-1])


