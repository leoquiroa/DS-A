import math

def getBillionUsersDay(growthRates):
    def bsearch(l, h):
        if l == h:
            return h

        mid = (l + h) // 2
        print(l,h,mid,mid-l)
        total = sum(g ** mid for g in growthRates)
        if total < target:
            return bsearch(mid + 1, h)
        else:
            return bsearch(l, mid)

    target = 10**9
    l = 1
    h = math.ceil(math.log(target, max(growthRates)))

    return bsearch(l, h)

if __name__ == '__main__':
    R = []
    R.append([1.5]) # 52
    R.append([1.1, 1.2, 1.3]) # 79
    R.append([1.01, 1.02]) # 1047
    
    for r in R:
        print(r,getBillionUsersDay(r))
        

    