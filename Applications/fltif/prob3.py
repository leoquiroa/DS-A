def solution(t, input_arr):
    # your code goes here
    input_arr.sort()
    if t in input_arr: return True
    else:
        return my_recursive(t,input_arr)

def my_recursive(t,input_arr):
    cut_arr = [x for x in input_arr if x<t]
    if len(cut_arr) == 0: return False
    cover = cut_arr[-1]
    time_left = t - cover
    print(t,cover,time_left)
    if time_left in cut_arr[:-1]: return True
    if time_left == 0: return True
    return my_recursive(time_left,cut_arr[:-1])

def main():
    R = []
    #R.append([10,[1,4,2,5,3,10]])
    R.append([10,[1,4,2,5,3]])
    R.append([10,[1,4,7]])
    for r in R:
        print(r,solution(r[0],r[1]))

if __name__=="__main__":
    main()

    