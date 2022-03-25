def solution(S):
    # write your code in Python 3.6
    block_no = 0
    stack = []
    for s in S:
        #1. if the stack is NOT empty and high -> low
        while len(stack)>0 and stack[-1] > s:
            stack.pop()
        #2. if the stack is empty
        if len(stack) == 0:
            block_no += 1
            stack.append(s)
        #3. if the height is the same, do nothing
        elif stack[-1] == s: continue
        #4. low -> high
        elif stack[-1] < s: 
            block_no += 1
            stack.append(s)        
    return block_no

if __name__ == '__main__':
    A = []
    A.append([8, 8, 8])
    A.append([8, 8, 5, 5])
    A.append([8, 8, 5, 7, 9, 8, 7])
    A.append([8, 8, 5, 7, 9, 8, 7, 4, 8])
    A.append([8, 8, 5, 7, 9, 8, 7, 5, 8])
    for a in A:
        print(a,solution(a))