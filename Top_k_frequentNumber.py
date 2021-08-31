"""Here we need to find k no of repeating/frequent element from the given array"""

import heapq
def topKfrequentNo(arr,k):
    pair=[]
    for i in arr:
        pair.append((arr.count(i),i))
    # using set to remove duplicates from the pair of list
    val=heapq.nlargest(k,set(pair))
    
    return [x[1]for x in val]
arr=[1,1,1,3,2,2,4]
k=2
print(topKfrequentNo(arr,k))