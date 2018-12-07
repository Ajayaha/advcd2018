'''
Created on 6 dec. 2018

@author: Ajayaha
'''
from builtins import range
from collections import Counter
from platform import dist

fileHandle = open('input.txt', 'r')
count = 0
point = [0, 0]
i = 0 

x, y = [], []
xmin = 0
ymin = 0
xmax = 0
ymax = 0
fdeviation = 1
intersect1 = {}
for fdeviation in range(1, 3):
    edeviation = 0
    for line in fileHandle:
        row = line.split()
        xval = int(row[0].strip(','))
        yval = int(row[1].strip('\n'))
        x.append(xval)
        y.append(yval)
       # print(xval)
        if (xmax < xval):
            xmax = xval
        if (ymax < yval):
            ymax = yval
        print(xval, yval)
    # print(xmax, ymax)
    
    maxvalue = max(xmax, ymax)
    xmax = ymax = maxvalue + fdeviation + edeviation
    values = []
    keys = []
    listofdist = []
    
    for k in range(1, 2):
        values.append([])
        keys.append([])
        finalarray = []
        for yval in range(0, ymax + k):
            finalarray.append([])
            # for xval in range(0, xmax + k):
            #    finalarray[yval].append(count)
            #    count = count + 1
            # for q in range(0, len(finalarray[yval])):
            #    print("%5s" % finalarray[yval][q], end='')
            # print()            
            
        for yval in range(0, ymax + k):
            for xval in range(0, xmax + k):
                dist = []
                for i in range(0, len(x)):
                    pxval = x[i] + fdeviation
                    pyval = y[i] + fdeviation
                    distance = abs(pxval - (xval)) + abs(pyval - (yval))
                    dist.append(distance)
            # for q in range(0, len(finalarray[yval])):
            #    print("%5s" % finalarray[yval][q], end='')
            # print()    
                # print(dist)    
                if(dist.count(min(dist)) == 1):
                    finalarray[yval].append(dist.index(min(dist)))
                else:
                    finalarray[yval].append('X')
            # for q in range(0, len(finalarray[yval])):
             #   print("%5s" % finalarray[yval][q], end='')
            # print()
        
        '''
        for i in range(0, len(x)):
            pxval = x[i]
            pyval = y[i]
            finalarray[pyval][pxval] = 'A'
            
        for yval in range(0, ymax + 1):     
             print(finalarray[yval])
           '''  
        
        dist = {}
        for i in range (0, ymax + k):
            cnt = Counter(finalarray[i])
            data = (cnt.most_common())
            # print(data)
            for j in range(0, len(data)):
                # print(data[j][0], data[j][1])
                if(data[j][0]) in dist:
                    dist[data[j][0]] = dist[data[j][0]] + data[j][1]
                else: 
                    dist[data[j][0]] = data[j][1]
    
        values.append([])
        keys.append([])
        # sambaprint(dist)
        listofdist.append(dist)
        # print("aaaaaa")
        # print(listofdist)
        
    # samba print(len(listofdist))
    
    intersect = listofdist[0]
    for h in range(0, len(listofdist) - 1):
        intersect = []
        for item in listofdist[h].keys():
            if item in listofdist[h + 1]:
                if(listofdist[h + 1].get(item) == listofdist[h].get(item)):
                    intersect.append(item)
        # sambaprint ("Intersects:", h, intersect)
    print("Intersects:", intersect)
    intersect1[fdeviation] = intersect

intersect = []
for h in range(1, len(intersect1)):
     for item in intersect1[h].keys():
         if item in intersect1[h + 1]:
             if(intersect1[h + 1].get(item) == intersect1[h].get(item)):
                 intersect.append(intersect1[h].get(item))
     # sambaprint ("Intersects:", h, intersect)
print("Intersects:", max(intersect))

