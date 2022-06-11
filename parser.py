def parse(file):
    x,y = [],[]
    f = open(file)
    for l in f:
        row = l.split()
        x.append(float(row[0]))
        y.append(float(row[1]))
    return (x,y)