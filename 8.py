with open("8_input.txt","r") as f:
    X = [l.rstrip("\n") for l in f.readlines()]
    
import numpy as np
import rich
from scipy.linalg import null_space
from string import ascii_letters,digits
Y = "".join(X)
node_names = ascii_letters+digits

def find_idxs(s,c):
    vals = [item  == c for item in s]
    res = []
    for i,v in enumerate(vals):
       if v == True:
           res.append(i)
    return res
import cmath
def get_antinodes(z0,z1):
    diff = z1-z0
    return (2*diff+z0,-2*diff+z1)

def combinations_2(l):
    if len(l) == 0 or len(l)==1:
        return []
    cmb = []
    for i,a in enumerate(l):
       for j in range(i+1,len(l)):
           b = l[j]
           cmb.append((a,b))
    return cmb
def decomplexify(z):
    return (int(z.real),int(z.imag))

# def get_abc(z0,z1):
    # x0,y0 = z0.real,z0.imag
    # x1,y1 = z1.real, z1.imag
    # if x1 == x0:
        # a = 1
        # b = 0
        # c = -x0
    # elif y1 == y0:
        # a = 0
        # b = 1
        # c = -y0    
    # else:
        # a = y1-y0
        # b = -(x1-x0)
        # c = y0*(x1-x0)-(y1-y0)*x0
    # return (a,b,c)
    
# def line_locus(z0,z1,zs):
    # a,b,c = get_abc(z0,z1)
    # return [z for z in zs if (a*z.real+b*z.imag+c)==0]
    
def line_locus(z0,z1,zs):
    return [z for z in zs if ((z-z0)/(z0-z1)).imag == 0]
d = {}
for name in node_names:
    for i, row in enumerate(X):
        js = find_idxs(row,name)
        if name in d:
            pass
        else:
            d[name] = []
        for j in js:
            d[name].append((i,j))

def is_within(t,height,widht):
    return t[0] in range(height) and t[1] in range(width)
height, width = len(X),len(X[0])
res = set()
for name,item in d.items():
    for t0,t1 in combinations_2(item):
        z0,z1 = complex(*t0),complex(*t1)
        antinodes = [decomplexify(z) for z in get_antinodes(z0,z1)]
        antinodes = [a for a in antinodes if is_within(a,height,width)]
        res = res.union(set(antinodes))
print(len(res))


res = set()
zs = [complex(i,j) for i in range(height) for j in range(width)]
for name,item in d.items():
    for t0,t1 in combinations_2(item):
        z0,z1 = complex(*t0),complex(*t1)
        antinodes = [decomplexify(z) for z in line_locus(z0,z1,zs)]
        res = res.union(set(antinodes))

