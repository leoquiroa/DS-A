

def solution(A):
    result = []
    ix_left,ix_right = 0,len(A)-1
    while ix_left != ix_right:
        left_val = abs(A[ix_left])
        right_val = abs(A[ix_right])
        if left_val not in result: result.append(left_val)
        if right_val not in result: result.append(right_val)
        ix_left += 1
        if ix_left == ix_right: break
        ix_right -= 1
        if ix_left == ix_right: break
    return len(result)
        
def solutionB(numbers):
    """Solution method implementation."""
    
    # variable initialization
    result = 0
    current, former = None, None
    front, back = len(numbers) - 1, 0

    # main while loop
    while front >= back:
        # move caterpillar's front backward
        if abs(numbers[front]) >= abs(numbers[back]):
            current = abs(numbers[front])
            front -= 1
        # move caterpillar's back forward
        else:
            current = abs(numbers[back])
            back += 1
        # increment distinct element count
        result += 1 if current != former else 0
        
        # prepare for next iteration        
        former = current

        print(former,current,back,front,numbers[back],numbers[front])

    return result    
 
if __name__ == '__main__':
    R = []
    R.append([-5,-3,-1,0,3,6])
    for r in R:
        print(r,solutionB(r))