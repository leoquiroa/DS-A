def solution(S):
    lines = S.split('\n')
    result = [lines[0]]
    for line in lines[1:]:
        cols = line.split(',')
        if 'NULL' not in cols:
            result.append(line)
    return "\n".join(result)

    #result = [x for x in lines if 'NULL' not in x]
    

if __name__ == '__main__':
    R = []
    R.append("id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11") 
    # "id,name,age,score\n17,Betty,28,11
    R.append("header,header\nANNUL,ANNULLED\nnull,NILL\nNULL,NULL") 
    # "header,header\nANNUL,ANNULLED\nnull,NILL"
    R.append("country,population,area\nUK,67m,242000km2") 
    # "country,population,area\nUK,67m,242000km2"
    for r in R:
        print(r,solution(r))
        

    