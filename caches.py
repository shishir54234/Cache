from itertools import repeat
from collections import defaultdict
import math
x=[[4,512,4],[4,2048,4]]
output = []
for i in x:
    way = i[0]
    cache_size = i[1]
    block_size = i[2]
    offset = int(math.log(block_size,2))
    ind = (cache_size)*1024 //(block_size * way)
    index_bits = int(math.log(ind,2))
    tag = 32 - index_bits - offset
    
    d = {}
    for i in range(ind):
        d[i]=[[] for x in repeat(None, way)]
    for i in range(ind):
        for j in range(way):
            d[i][j].append(0)
    f = open('gzip.trace','r')
    lines=f.readlines()
    hit=0
    miss=0
    for k in range(len(lines)):
        found=0
        x=int(lines[k][2:12], 0)#[2:12]
        x=x>>offset
        index=x%(ind)
        #print(index)
        tag=x>>index_bits
        #print(tag)
        for l in range(way):
            if(d[index][l][0]==1):
                if(d[index][l][1]==tag):
                    found=found+1
                    d[index].pop(l)
                    d[index].append([1,tag])
                    break
        if(found==0):
            added=0
            for l in range(way): 
                if(d[index][l][0]==0):
                    d[index].pop(l)
                    d[index].append([1,tag])
                    added=1
            if(added!=1):
                d[index].pop(0)
                d[index].append([1,tag])
            miss=miss+1
        if(found==1):
            hit=hit+1

    print( (hit/(hit+miss))*100)
    # print(hit)

    


    




