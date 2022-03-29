def matching_pairs(s, t):
    if s == t: return len(s)-2

    diff_s,diff_t = [],[]
    #only different
    for i in range(0,len(s)):
        if s[i] != t[i]: 
            diff_s.append(s[i])
            diff_t.append(t[i])


    for ix_s,d in enumerate(diff_s):
        if d not in diff_t: continue
        ix_t = diff_t.index(d)
        if d==diff_t[ix_t] and diff_t[ix_s]==diff_s[ix_t]:
            del diff_s[ix_t]
            del diff_s[ix_s]
            break
    
    return len(s) - len(diff_s)
        



if __name__ == '__main__':
    R = []
    R.append(["abcdefghi", "aicfedghb"]) #7
    R.append(["abcde", "adcbe"]) #5
    R.append(["abcd", "abcd"]) #2
    R.append(["abcd", "adcb"]) #4
    R.append(["mno", "mno"]) #1
    for r in R:
        print(r,matching_pairs(r[0],r[1]))
        

    