import struct
def readParameters():

    with open("C:/Users/user/Desktop/hw4_v5/hw4/input/problem1/input3",'rb') as fin:
        (m,) = struct.unpack("i",fin.read(4)) 
        (n,) = struct.unpack("i",fin.read(4))
        v = [[0]*(m+1) for i in range(n)]
        h = [[0]*(m) for i in range(n+1)]
        for i in range(n):
            for j in range(m+1):
                (v[i][j],) = struct.unpack("d",fin.read(8))
        for i in range(n+1):
            for j in range(m):
                (h[i][j],) = struct.unpack("d",fin.read(8))
    return m, n, v, h

import numpy as np
def main():
    (m, n, v, h) = readParameters()
    vert = [[2000]*(m+1) for i in range(n+1)]  #set a big enough number as infinity(vertical)
    path = [['']*(m+1) for i in range(n+1)]  #record path
    vert[0][0]=0  #starting point
    x, y = 0, 0
    temp = [[vert[0][0],0,0]]
    valid = []
    while x!=n or y!=m:
        if x!= n:
            down = vert[x][y] + v[x][y]
            if down < vert[x+1][y]:
                if [vert[x+1][y],x+1,y] in temp:
                    temp.remove([vert[x+1][y],x+1,y])
                vert[x+1][y], path[x+1][y] = down, 'd'
                temp.append([vert[x+1][y],x+1,y])
        if x!=0:
            up = vert[x][y] + v[x-1][y]
            if up < vert[x-1][y]:
                if [vert[x-1][y],x-1,y] in temp:
                    temp.remove([vert[x-1][y],x-1,y])
                vert[x-1][y], path[x-1][y] = up, 'u'
                temp.append([vert[x-1][y],x-1,y])
        if y!=m:
            right = vert[x][y] + h[x][y]
            if right < vert[x][y+1]:
                if [vert[x][y+1],x,y+1] in temp:
                    temp.remove([vert[x][y+1],x,y+1])
                vert[x][y+1], path[x][y+1] = right, 'r'
                temp.append([vert[x][y+1],x,y+1])
        if y!=0:
            left = vert[x][y] + h[x][y-1]
            if left < vert[x][y-1]:
                if [vert[x][y-1],x,y-1] in temp:
                    temp.remove([vert[x][y-1],x,y-1])
                vert[x][y-1], path[x][y-1] = left, 'l'
                temp.append([vert[x][y-1],x,y-1])
        temp.remove([vert[x][y],x,y])
        minim = 2000   #find the minimum path
        index = 0
        for i in range(len(temp)):
            if temp[i][0] < minim:
                minim = temp[i][0]
                index = i
        x, y = temp[index][1], temp[index][2]

    route = ''
    x, y = n, m
    while path[x][y] != '':
        if path[x][y] == 'u':
            route += path[x][y]
            x += 1
        if path[x][y] == 'd':
            route += path[x][y]
            x -= 1
        if path[x][y] == 'l':
            route += path[x][y]
            y += 1
        if path[x][y] == 'r':
            route += path[x][y]
            y -= 1
            
    real = []
    for i in range(len(route)):
        real.append(route[-1-i])
        rou = ''.join(real)
    print(vert[n][m], rou)

main()