def solution(S):
    # write your code in Python 3.6
    if len(S) == 0 : return 1
    stack = []
    guide = {
        ")":"("
        ,"]":"["
        ,"}":"{"        
    }
    for s in S:
        if s in guide and len(stack)>0:
            val = stack.pop()
            if val == guide[s]: continue
            else: return 0
        else:
            stack.append(s)
    return 1 if len(stack)==0 else 0

if __name__ == '__main__':
    A = []
    A.append("{[()()]}")
    A.append("([)()]")
    A.append(")(")
    for a in A:
        print(a,solution(a))