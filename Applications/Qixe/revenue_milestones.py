
def getMilestoneDaysA(revenues, milestones):
    expected = []
    ix = -1
    aux = 0
    for milestone in milestones:
        while ix < len(revenues):
            ix += 1
            aux += revenues[ix]
            if aux >= milestone:
               expected.append(ix+1) 
               break
            if ix == len(revenues): expected.append(-1) 
        if len(expected) == len(milestones): break
    return expected

def getMilestoneDaysB(revenues, milestones):
    days = [-1]*len(milestones)
    sum_each_day = [revenues[0]]
    for revenue in revenues[1:]:
        sum_each_day.append(sum_each_day[-1]+revenue)
    for ix,milestone in enumerate(milestones):
        tmp = [ii+1 for ii,x in enumerate(sum_each_day) if x>=milestone]
        days[ix] = tmp[0] if len(tmp) > 0 else -1
    return days

if __name__ == '__main__':
    R = []
    R.append([[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],[100, 200, 500]]) # [4, 6, 10]
    R.append([[100, 200, 300, 400, 500],[300, 800, 1000, 1400]]) # [2, 4, 4, 5]
    R.append([[700, 800, 600, 400, 600, 700],[3100, 2200, 800, 2100, 1000] ]) # [5, 4, 2, 3, 2]
    for r in R:
        print(r,getMilestoneDaysB(r[0],r[1]))
        

    