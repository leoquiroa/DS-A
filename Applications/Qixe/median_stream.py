

def findMedian1(arr):
    result = []
    result.append(arr[0])
    ix = 2
    while ix < len(arr)+1:
        tmp = arr[:ix]
        tmp.sort()
        ix_mid = int(len(tmp)/2)
        if (len(tmp)%2)==0:
            val = int(sum(tmp[ix_mid-1:ix_mid+1])/2)
        else:
            val = tmp[ix_mid]
        result.append(val)
        ix += 1
    return result

import heapq

def findMedian(arr):
    small_half = [] #(i+1)//2 + (i+1)%2 elements, max heap
    large_half = [] #(i+1)//2 elements, min heap
    ret = []
    for i,x in enumerate(arr):
        # i even then increase the size of small_half
        # i odd then increase the size of large_half
        if i%2 == 0:
            val = -heapq.heappushpop(large_half,x)
            heapq.heappush(small_half, val)
            ret.append(-small_half[0])
        else:
            val = -heapq.heappushpop(small_half,-x)
            heapq.heappush(large_half, val)
            ret.append((large_half[0]-small_half[0])//2)
    return ret

if __name__ == '__main__':
    R = []
    R.append([5, 15, 1, 3]) # [5, 10, 5, 4]
    R.append([2, 4, 7, 1, 5, 3]) # [2, 3, 4, 3, 4, 3]
    R.append([1, 2]) # [1, 1]
    for r in R:
        print(r,findMedian(r))
        

    