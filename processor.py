from parser import parse
from util import slope

def process(fileA, fileB):
    a_slopes,b_slopes = [],[]
    Ax,Ay = parse(fileA)
    Bx,By = parse(fileB)

    for i in range(0,(len(Ax)-5)):
        Ax1 = Ax[i]
        Ay1 = Ay[i]
        Ax2 = Ax[i+5]
        Ay2 = Ay[i+5]
        
        Bx1 = Bx[i]
        By1 = By[i]
        Bx2 = Bx[i+5]
        By2 = By[i+5]
        a_slopes.append(slope(Ax1,Ay1,Ax2,Ay2))
        b_slopes.append(slope(Bx1,By1,Bx2,By2))
    
    if str(a_slopes) == str(b_slopes):
        print("the same")
    else:
        print("diff")