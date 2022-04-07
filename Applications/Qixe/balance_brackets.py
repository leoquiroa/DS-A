def isBalanced(S):
    # write your code in Python 3.6
    if len(S) == 0 : return True
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
            else: return False
        else:
            stack.append(s)
    return True if len(stack)==0 else False

if __name__ == '__main__':
    A = []
    A.append("{[()()]}")    # True
    A.append("([)()]")      # False
    A.append(")(")          # False
    A.append("{[()]}")      # True
    A.append("{}()")        # True
    A.append("{(})")        # False
    A.append(")")           # False
    for a in A:
        print(a,isBalanced(a))