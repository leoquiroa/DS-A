
def canGetExactChange(targetMoney, denominations):
    if targetMoney in denominations: 
        return True
    new_list = [x for x in denominations if x < targetMoney]
    if len(new_list) == 1 and targetMoney > new_list[0]: 
        return False
    falta = targetMoney % new_list[-1]
    if falta == 0: 
        return True
    return canGetExactChange(falta, new_list[:-1])
    

if __name__ == '__main__':
    R = []
    R.append([95, [5, 10, 25, 100, 200]]) # True
    R.append([94, [5, 10, 25, 100, 200]]) # False
    R.append([75, [4, 17, 29]]) # True
    for r in R:
        print(r,canGetExactChange(r[0],r[1]))
        

    