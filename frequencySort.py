"""This is same as top k frequent no question here we sort values based on frequency of the element in the 
array"""

import heapq
def frequency(arr):
    val=[]
    for i in arr:
        val.append((arr.count(i),i))
    data=heapq.nlargest(len(arr),val)
    return [x[1]for x in data]

arr=[1,1,1,3,2,2,4]
print(frequency(arr))