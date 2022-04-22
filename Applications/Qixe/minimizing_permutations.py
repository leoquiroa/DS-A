
import collections

def minOperationsA(arr):
    target = "".join([str(num) for num in sorted(arr)])
    curr = "".join([str(num) for num in arr])
    queue = collections.deque([(0, curr)]) # In the queue we store (<level>, <permutation>)
    visited = set([curr])

    while queue:
        level, curr = queue.popleft()

        if curr == target:
            return level # We are done

        for i in range(len(curr)):
            for j in range(i, len(curr)):
                # Reverse elements between i and j (inclusive)
                # Note we are operating on strings here, so we create a new copy
                permutation = curr[:i] + curr[i:j + 1][::-1] + curr[j + 1:]
                if permutation == target: return level + 1
                if permutation not in visited:
                    visited.add(permutation)
                    queue.append((level + 1, permutation))
            #print('i ',i)
        
        #print('len(queue) ',len(queue))
          
    return -1

def minOperations(arr):
    goal = ''.join(str(c) for c in sorted(arr))
    start = ''.join(str(c) for c in arr)
    q = collections.deque([start])
    visited = set([start])
    levels = 0

    while q:
        for _ in range(len(q)):
            currWord = q.popleft()
            
            if currWord == goal:
                return levels # currWord is sorted, return how many levels deep in the BFS.
            
            for i in range(len(arr)):
                for j in range(i + 1, len(currWord)):
                    chars = [c for c in currWord]
                    chars[i:j+1] = chars[i:j+1][::-1] # reverse the sublist
                    nextWord = ''.join(chars)
                    if nextWord not in visited:
                        visited.add(nextWord)
                        q.append(nextWord)
                    chars[i:j+1] = chars[i:j+1][::-1] # revert the sublist back to original node state

        levels += 1
        
    return -1    

if __name__ == '__main__':
    R = []
    R.append([3, 1, 2]) # 2
    R.append([1, 2, 5, 4, 3]) # 1
    for r in R:
        print(r,minOperations(r))
        

    