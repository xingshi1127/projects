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
land = n.replace('\n',' ').replace(' ','$').strip().split('$')
while(land.count('')):
    land.remove('')
for _ in range(len(land)):
    land[_] = int(land[_])
dex = 0
tri = [[0]*line for x in range(line)]
for i in range(line):
    for j in range(i+1):
        tri[i][j] = land[dex]
        dex += 1
largest = 0
left = []
num = 0
alist = [[[0,[],0] for x in range(line)] for y in range(line)]
def getlist(i,j):
    if i == line -1:
        return [tri[i][j],[tri[i][j]],1]
    else:
        if alist[i+1][j][0] > alist[i+1][j+1][0]:
            q = []
            q = alist[i+1][j][1].copy()               
            q.insert(0,tri[i][j])
            return [tri[i][j]+alist[i+1][j][0],q,alist[i+1][j][2]]
        elif alist[i+1][j][0] < alist[i+1][j+1][0]:
            q = alist[i+1][j+1][1].copy()
            q.insert(0,tri[i][j])
            return [tri[i][j]+alist[i+1][j+1][0],q,alist[i+1][j+1][2]]
        elif alist[i+1][j][0] == alist[i+1][j+1][0]:
            q = alist[i+1][j][1].copy()               
            q.insert(0,tri[i][j])
            
            return [tri[i][j]+alist[i+1][j][0],q,alist[i+1][j][2]+alist[i+1][j+1][2]]
           

for i in range(line-1,-1,-1):
    for j in range(i+1):
        alist[i][j] = getlist(i,j)
        

largest = alist[0][0][0]
left = alist[0][0][1]
num = alist[0][0][2]
print('The largest sum is: {}'.format(largest))
print('The number of paths yielding this sum is: {}'.format(num))
print('The leftmost path yielding this sum is: {}'.format(left))


