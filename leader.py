# Leaders In array:
# An element which is greater than all elements to its right is leader

def leader(a):
    max = -999
    leaderArr = []
    for i in reversed(range(len(a))):
        if a[i] > max:
            leaderArr.append(a[i])
            max = a[i]
    print(leaderArr)
    
leader([16,17,4,3,5,2])
