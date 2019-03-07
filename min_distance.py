#find the closes numbers (to each other) in a list and return there values

ranlist = [321345, 1534562, 1302932, 3712314, 12134, 32452350, 23452372]



def minDistance(lst):
    lst = sorted(lst)
    index = -1
    distance = max(lst) - min(lst)
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] < distance:
            distance = lst[i+1] - lst[i] 
            index = i
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] == distance:
            return lst[i],lst[i+1]


a,b = minDistance(ranlist)

print(a)
print(b)