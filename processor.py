from parser import parse
from util import slope
from grapher import graph

def walk(sfA, sfB):
    alike_segs = []
    diff_segs = []
    cur_seg = []
    
    err = .001
    length = min(len(sfA),len(sfB))
    left = 0
    right = 0

    flag = False
    sflag = False
    dflag = False
    while(left < length):
        #true if slopes are the 'same', else false
        cmp = abs(sfA[left]-sfB[left]) < err

        #'same' slope and haven't started a segment
        if(cmp and not flag):
            flag = True
            sflag = True
            cur_seg.append(left)
       
        #'different' slope and haven't started a segment
        if (not cmp and not flag):
            flag = True
            dflag = True
            cur_seg.append(left)
        
        #in a segment of similar slopes and find a nonequal 
        if (sflag and not cmp):
            flag = False
            sflag = False
            cur_seg.append(left-1)
            alike_segs.append(cur_seg)
            cur_seg = []
            left -= 1
        
        #in a segment of diff slopes and find an equal 
        if (dflag and cmp):
            flag = False
            dflag = False
            cur_seg.append(left-1)
            diff_segs.append(cur_seg)
            cur_seg = []
            left -= 1
        
        left += 1
    
    #reached end in a segment
    if flag:
        if sflag:
            cur_seg.append(left-1)
            alike_segs.append(cur_seg)
        else:
            cur_seg.append(left-1)
            diff_segs.append(cur_seg)
    return (alike_segs,diff_segs)


def process(fileA, fileB):
    a_slopes,b_slopes = [],[]
    aX,aY = parse(fileA)
    bX,bY = parse(fileB)

    window = 5
    for i in range(0,(len(aX)-window)):
        aX1 = aX[i]
        aY1 = aY[i]
        aX2 = aX[i+window]
        aY2 = aY[i+window]
        
        bX1 = bX[i]
        bY1 = bY[i]
        bX2 = bX[i+window]
        bY2 = bY[i+window]
        a_slopes.append(slope(aX1,aY1,aX2,aY2))
        b_slopes.append(slope(bX1,bY1,bX2,bY2))
    
    #print(diff(a_slopes,b_slopes))
    a,d = walk([1,2,3,2,1,55,56,57,8],[1,2,30,20,10,55,56,57,9])
    graph(aX,aY,bX,bY,a,d)

def diff(a,b):
    total_dif = 0.0
    for i,j in zip(a,b):
        dif = i-j
        total_dif += dif
    total_dif /= len(a)
    return total_dif
