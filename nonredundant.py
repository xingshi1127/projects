from collections import deque
pipe = deque()
import sys
try:
    filename = input('Which data file do you want to use? ')
    file = open(filename)
except:
    print('There is no such file as '+filename)
    sys.exit()

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
end = []
for x in alist[1]:
    index = 0
    for y in alist[0]:
        if x != y:
            index += 1
        if index == line:
            end.append(x)
endpoint = list(set(end))
startlist = []
startlist = list(set(alist[0]))
dex = 0
iii = 0
redundancy = []

for i in startlist:
    possible = {}
    poss = []
    for _ in range(line):
        if alist[0][_] == i:

            pipe.appendleft(alist[1][_])
            possible[alist[1][_]]= 1
            poss.append(alist[1][_])
           

    dex = pipe[-1]
    finallist = []
    while len(pipe) != 0:
        if dex in possible:
            if possible[dex] >= 2:
                pipe.pop()
                if len(pipe) == 0:
                    continue
                else:
                    dex = pipe[-1]

                
        if dex not in endpoint:
            #print('finsh',dex)
            for _ in range(line):
                if alist[0][_] == dex:
                    pipe.appendleft(alist[1][_])
                    if alist[1][_] in possible:
                        possible[alist[1][_]] = 1 + possible[alist[1][_]]

                    else:
                        possible[alist[1][_]] = 1

                    
            pipe.pop()
            dex = pipe[-1] 
         
        else:
            pipe.pop()

            if len(pipe) == 0:

                continue
            else:
                dex = pipe[-1]
     
    for k in possible:
        if possible[k] >= 2:
            finallist.append(k)
    for _ in finallist:
        if _ in poss:
            redundancy.append([i,_])
final = [redundancy[i] for i in range(len(redundancy)) if redundancy[i] not in redundancy[:i]]
print('The nonredundant facts are:')
for i in range(line):
    if [alist[0][i],alist[1][i]] not in redundancy:
        print('R({},{})'.format(alist[0][i],alist[1][i]))
        

        
        
                    
     
                    
    
    
