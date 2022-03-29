from functools import reduce

def solution(input_arr):
    # your code goes here
    return reduce((lambda x,y: x*y),input_arr)
    

def main():
    R = []
    R.append([1,3,4])
    R.append([1,2,5,13])
    for r in R:
        print(r,solution(r))

if __name__=="__main__":
    main()

    