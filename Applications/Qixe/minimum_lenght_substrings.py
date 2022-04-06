from collections import Counter

def check_(count1,count2):
  for key in count2:
    if count1.get(key,0)<count2[key]:
      return False
  return True

def min_length_substring(s, t):
  # Write your code here
  s_count = Counter(s)
  t_count = Counter(t)
  
  if not check_(s_count,t_count):
    return -1
  
  left,right = 0, len(s)-1
  
  while left<right:
    if s_count[s[left]] <= t_count.get(s[left],0):
      break
    s_count[s[left]] -=1
    left+=1
    
  while left<right:
    if s_count[s[right]] <= t_count.get(s[right],0):
      break
    s_count[s[right]] -=1
    right-=1
  
  return right-left+1

if __name__ == '__main__':
    R = []
    R.append(["zcdbefebce","fd"]) # 4
    R.append(["dcbefebce","fd"]) # 5
    R.append(["ababcb","abc"]) # 3
    R.append(["efecfefdz","dcz"]) # 6
    R.append(["bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf","cbccfafebccdccebdd"]) # -1
    for r in R:
        print(r,min_length_substring(r[0],r[1]))
        

    