def solution(A):
    # write your code in Python 3.6
    counter = 0
    is_zero = len([x for x in A if x == 0])
    for ix,a in enumerate(A):
        if is_zero == 0: break
        if a == 0:
            counter += len([x for x in A[ix+1:] if x == 1])
        else: 
            continue
        is_zero -= 1
    if counter > 1000000000: return -1
    return counter

def solutionB(A):
    #initialize pairs to zero
     pairs = 0
     #count the numbers of zero discovered while traversing 'A'
     #for each successive '1' in the list, number of pairs will
     #be incremented by the number of zeros discovered before that '1'
     zero_count = 0
     #traverse through the list 'A'
     for i in range(0, len(A)):
         if A[i] == 0:
             #counting the number of zeros discovered
             zero_count += 1
         elif A[i] == 1:
             #if '1' is discovered, then number of pairs is incremented
             #by the number of '0's discovered before that '1'
             pairs += zero_count
             #if pairs is greater than 1 billion, return -1
             if pairs > 1000000000:
                 return -1
    #return number of pairs
     return pairs


if __name__ == '__main__':
    A = []
    A.append([0, 1, 0, 1, 1])
    for a in A:
        print(a,solutionB(a))