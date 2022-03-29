import math

class record:
    def __init__(self,i,v) -> None:
        self.index = i
        self.value = v

def findPositions(arr, x):
    clss_arr = [record(i,x) for i,x in enumerate(arr)]
    output = []
    for i in range(0,x):
        # step 1
        if x < len(clss_arr): 
            popped = clss_arr[:x]
            clss_arr = clss_arr[x:]
        else:
            popped = clss_arr
            clss_arr = []
        # step 2
        tmp = [x.value for x in popped]
        largest = max(tmp)
        ix = tmp.index(largest)
        output.append(popped[ix].index+1)
        del popped[ix]
        # step 3
        popped = [record(x.index,x.value-1) 
                if x.value > 0 
                else record(x.index,x.value) 
                for x in popped]
        clss_arr += popped
    return output

if __name__ == '__main__':
    R = []
    R.append([[1, 2, 2, 3, 4, 5],5]) #[5, 6, 4, 1, 2]
    R.append([[2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4],4]) #[2, 5, 10, 13]
    for r in R:
        print(r,findPositions(r[0],r[1]))
        

    