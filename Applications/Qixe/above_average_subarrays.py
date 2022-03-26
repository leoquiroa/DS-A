import math

def aboveAverageSubarrays(A):
    big_total = sum(A)
    output = []
    for i in range(len(A)):
        for j in range(i,len(A)):
            sub_total = sum(A[i:j+1])
            sub_den = (j-i+1)
            all_total = big_total-sub_total
            all_den = len(A)-sub_den if sub_den < len(A) else 1 
            if all_total/all_den < sub_total/sub_den:
                output.append([i+1,j+1])
    return output

if __name__ == '__main__':
    R = []
    R.append([3, 4, 2]) # [[1, 2], [1, 3], [2, 2]]
    for r in R:
        print(r,aboveAverageSubarrays(r))
        

    