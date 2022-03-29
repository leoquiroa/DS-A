import math 

def solution(n):
    # your code goes here
    N = 13
    times = math.floor(n/N)
    return n-times

def main():
    R = [12,14,25,27]
    R = [x for x in range(0,50)]
    for r in R:
        print(r,solution(r))
    #n = int(input().strip())
    #result = solution(n)

    #print(result)

if __name__=="__main__":
    main()

    