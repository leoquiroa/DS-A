
from operator import index


def canGetExactChange(targetMoney, denominations):
    if targetMoney in denominations: 
        return True
    new_list = [x for x in denominations if x < targetMoney]
    vuelto = [targetMoney % x for x in new_list]
    if 0 in vuelto: return True
    val = min(vuelto)
    del new_list[new_list.index(val)]
    return canGetExactChange(vuelto, new_list)
    
    
    

if __name__ == '__main__':
    R = []
    R.append([95, [5, 10, 25, 100, 200]]) # True
    R.append([94, [5, 10, 25, 100, 200]]) # False
    R.append([75, [4, 17, 29]]) # True
    R.append([60, [5, 20, 25]]) # True
    R.append([60, [20, 25]]) # True
    for r in R:
        print(r,canGetExactChange(r[0],r[1]))
        

    