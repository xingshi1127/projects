from collections import deque
breakpoint = 0
def selectlist(a):
    blist = a
    clist = []
    qlist = []
    num = 0
    for i in a:
        for _ in range(line):
            if alist[0][_] == i[len(i)-1]:
                qlist = i.copy()
                qlist.append(alist[1][_])
                clist.append(qlist) 
    for i in clist:
        for _ in endpoint:
            if i[len(i)-1] == _:
                finallist.append(i)
    return clist
finallist = []
pipe = deque()
try:
    file = open('partial_order.txt').readlines()
except:
    print('erro')
    exit
n = ''
line = 0
for _ in file:
    if _.find('\n'):
        line += 1
    n += _
land = n.replace('\n',',').replace('R(','').replace(')','').strip().split(',')

while(land.count('')):
    land.remove('')
alist = [[] for x in range(2)]
for _ in range(0,len(land)):
    land[_] = int(land[_])
for i in range(0,len(land),2):
    alist[0].append(land[i])
    alist[1].append(land[i+1])
start = []
end = []

for x in alist[0]:
    index = 0
    for y in alist[1]:
        if x != y:
            index += 1
        if index == line:
            start.append(x)
for x in alist[1]:
    index = 0
    for y in alist[0]:
        if x != y:
            index += 1
        if index == line:
            end.append(x)
startpoint = list(set(start))
endpoint = list(set(end))
print('finish')
for i in startpoint:
    dlist = [[i]]
    while True:
        mlist = dlist.copy()
        dlist = selectlist(dlist)
        if  mlist == dlist:
            break
print('finish2')
alllist = [finallist[i] for i in range(len(finallist)) if finallist[i] not in finallist[:i]]
tree = []
temple = []
print('finish3')
for i in alllist:
    for j in alllist:
        if i[0] == j[0] and i[len(i)-1] == j[len(j)-1]:
            if len(j) > len(i):
                temple = j
    tree.append(temple)
    
tree = [tree[i] for i in range(len(tree)) if tree[i] not in tree[:i]]
success = []
redundency = []
print('finish3')
for _ in tree:
    for i in range(len(_)-1):
        success.append([_[i],_[i+1]])
for i in range(line):
    redundency = [i for i in success if i in success]            
print([redundency[i] for i in range(len(redundency)) if redundency[i] not in redundency[:i]])
