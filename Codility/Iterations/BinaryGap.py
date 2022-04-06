def solution(n):
    num = bin(n).replace("0b", "")
    line = [int(x) for x in num]
    
    gaps = []
    paral = False
    counter = 0
    
    if 0 not in line: return 0
    
    for e in line:
        if e == 1:
            paral = True
            
            if counter > 0:
                gaps.append(counter)
                counter = 0
        elif e == 0:
            if paral is True: counter += 1

    if len(gaps) == 0: return 0
    return max(gaps)

if __name__ == '__main__':
    N = [9,529,20,1041,15,32]
    for n in N:
        print(n,solution(n))