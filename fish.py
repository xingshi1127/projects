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
dis_fish = [[] for x in range(2)]
for i in range(0,len(land),2):
    dis_fish[0].append(land[i])
    dis_fish[1].append(land[i+1])
for i in range(line-1,0,-1):
    dis_fish[0][i] = dis_fish[0][i] - dis_fish[0][i-1]
dis_fish[0][0] = 0
sort_fish = sorted(dis_fish[1])
beginning = sort_fish[0]
end = sort_fish[len(sort_fish)-1]
start = int((beginning + end) / 2)
sum_fish = dis_fish[1][0] - start
q = 0
while True:
    q = start
    
    for i in range(line-1):
        if sum_fish != 0:
            if sum_fish < dis_fish[0][i+1] and sum_fish > 0:
                sum_fish = dis_fish[1][i+1] - start
            else:
                sum_fish = dis_fish[1][i+1] - dis_fish[0][i+1] + sum_fish - start

        else:
            sum_fish = dis_fish[1][i+1] - start
      

    if sum_fish < 0:
        end = start
        start = int((end +beginning)/2)       
    elif sum_fish > 0:
        beginning = start
        start = int((beginning + end)/2)      
    elif sum_fish == 0:
        break
    sum_fish = dis_fish[1][0] - start
    if q == start:
        break
print('The maximum quantity of fish that each town can have is {}.'.format(start))

    


    

    
