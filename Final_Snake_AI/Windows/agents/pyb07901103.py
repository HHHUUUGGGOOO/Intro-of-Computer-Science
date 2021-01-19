import ctypes
import sys
import random

MOVE = {
    'noAct': 0,
    'U_Act': 1,
    'D_Act': 2,
    'L_Act': 3,
    'R_Act': 4,
    'ACC_Act': 5    #acceleration
}

class view:
    def __init__(self,map):
        self.map = map
        self.isFood = self.getFood(3)
        self.isWall = self.getWall(3)
        self.isBody = self.getBody(3)
        
    def getFood(self,rad):
        isFood = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == ".":
                    isFood = isFood + [1]
                else:
                    isFood = isFood + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == ".":
                    isFood = isFood + [1]
                else:
                    isFood = isFood + [0]
        else:
            for x in range(49):
                if self.map[x] == ".":
                    isFood = isFood + [1]
                else:
                    isFood = isFood + [0]
        self.isFood = isFood
        return isFood


    def getWall(self,rad):
        isWall = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == "#":
                    isWall = isWall + [1]
                else:
                    isWall = isWall + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == "#":
                    isWall = isWall + [1]
                else:
                    isWall = isWall + [0]
        else:
            for x in range(49):
                if self.map[x] == "#":
                    isWall = isWall + [1]
                else:
                    isWall = isWall + [0]

        self.isWall = isWall
        return isWall

    def getBody(self,rad):
        isBody = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == "*":
                    isBody = isBody + [1]
                else:
                    isBody = isBody + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == "*":
                    isBody = isBody + [1]
                else:
                    isBody = isBody + [0]
        else:
            for x in range(49):
                if self.map[x] == "*":
                    isBody = isBody + [1]
                else:
                    isBody = isBody + [0]
        self.isBody = isBody
        return isBody
    
    def getHead(self,rad):
        isHead = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == "@":
                    isHead = isHead + [1]
                else:
                    isHead = isHead + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == "@":
                    isHead = isHead + [1]
                else:
                    isHead = isHead + [0]
        else:
            for x in range(49):
                if self.map[x] == "@":
                    isHead = isHead + [1]
                else:
                    isHead = isHead + [0]
        self.isHead = isHead
        return isHead

class pyAgent:
    def __init__(self):
        view = []
    # void getView(int rad);
    # void getFoodInView(int rad);
    # void getSnakeInView(int rad);
    
    def isOppDir(self, a1, a2):
        if (a1 == U_Act and a2 == D_Act) or (a1 == D_Act and a2 == U_Act) or (a1 == R_Act and a2 == L_Act) or (a1 == L_Act and a2 == R_Act) :
            return true
        return false
    
    
def randMove():
    r = random.randint(0,6)
    # 2/6%: just go ahead
    # 4/6%: 1/6% for each direction
    
    if( r == 0 ):
        return MOVE['noAct']
    elif( r == 1 ):
        return MOVE['U_Act']
    elif( r == 2 ):
        return MOVE['D_Act']
    elif( r == 3 ):
        return MOVE['L_Act']
    elif( r == 4 ):
        return MOVE['R_Act']
    elif( r == 5 ):
        return MOVE['ACC_Act']
    else:
        return MOVE['noAct']

# !! TODO 5: implement your own actionToDo function here
def actionToDo(arg):
    # !! Here are some example for python to get view
    map = f.readline()
    # print("map",map)
    
    View = view(map)
    View.getFood(2)
    View.getWall(2)
    
    food_3 = View.getFood(3)
    
    wall_1 = View.getWall(1)
    wall_2 = View.getWall(2)
    wall_3 = View.getWall(3)
    
    body_3 = View.getBody(3)
    body_1 = View.getBody(1)

    head_3 = View.getHead(3)
    
    #evaluate the food density
    n_1, n_2, n_3, n_4 = 0, 0, 0, 0
    a, b, c, d = 0, 0, 0, 0
    for i in range(3):
        n_1 = n_1 + food_3[7*i] + food_3[1+7*i] + food_3[2+7*i]
        n_2 = n_2 + food_3[4+7*i] + food_3[5+7*i] + food_3[6+7*i]
        n_3 = n_3 + food_3[28+7*i] + food_3[29+7*i] + food_3[30+7*i]
        n_4 = n_4 + food_3[32+7*i] + food_3[33+7*i] + food_3[34+7*i]
    a, b, c, d = n_1+n_2, n_3+n_4, n_1+n_3, n_2+n_4
    move = {a:1, b:2, c:3, d:4}
    move_2 = {17:1, 31:2, 23:3, 25:4}
    direc = {1:'U_Act', 2:'D_Act', 3:'L_Act', 4:'R_Act'}

    #first we see the rad==3
    if 1 in food_3:
        if food_3[3] == 1 or food_3[10] == 1 or food_3[17] == 1:
            return 1
        elif food_3[21] == 1 or food_3[22] == 1 or food_3[23] == 1:
            return 3
        elif food_3[31] == 1 or food_3[38] == 1 or food_3[45] == 1:
            return 2
        elif food_3[25] == 1 or food_3[26] == 1 or food_3[27] == 1:
            return 4

    #To avoid the head 
    if head_3[17] == 1:
        if body_3[10] == 1:
            if wall_3[23] == 0 and body_3[23] == 0:
                return 3
            if wall_3[25] == 0 and body_3[25] == 0:
                return 4
    if head_3[23] == 1:
        if body_3[22] == 1:
            if wall_3[17] == 0 and body_3[17] == 0:
                return 2
            if wall_3[31] == 0 and body_3[31] == 0:
                return 1
    if head_3[25] == 1:
        if body_3[26] == 1:
            if wall_3[17] == 0 and body_3[17] == 0:
                return 2
            if wall_3[31] == 0 and body_3[31] == 0:
                return 1
    if head_3[31] == 1:
        if body_3[38] == 1:
            if wall_3[23] == 0 and body_3[23] == 0:
                return 3
            if wall_3[25] == 0 and body_3[25] == 0:
                return 4

    #To avoid the body
    #body corner
    if body_3[25] == 1 and body_3[31] == 1 and body_3[32] == 1:
        if body_3[17] == 1:
            return 3
        if body_3[23] == 1:
            return 1
    if body_3[23] == 1 and body_3[30] == 1 and body_3[31] == 1:
        if body_3[17] == 1:
            return 4
        if body_3[25] == 1:
            return 1
    if body_3[16] == 1 and body_3[17] == 1 and body_3[23] == 1:
        if body_3[25] == 1:
            return 2
        if body_3[31] == 1:
            return 4
    if body_3[17] == 1 and body_3[18] == 1 and body_3[25] == 1:
        if body_3[23] == 1:
            return 2
        if body_3[31] == 1:
            return 3

    #don't be close to the body
    if body_3[17] == 1 and body_3[31] == 1:
        if body_3[16] == 1 and body_3[18] == 1:
            if body_3[16] == 1 and body_3[18] == 1:
                if body_3[15] == 1 and body_3[19] == 0:
                    return 4
                if body_3[15] == 0 and body_3[19] == 1:
                    return 3
                if body_3[15] == 1 and body_3[19] == 1:
                    if body_3[14] == 1 and body_3[20] == 0:
                        return 4
                    if body_3[14] == 0 and body_3[20] == 1:
                        return 3
                    if body_3[14] == 0 and body_3[20] == 1:
                        return 4
    if body_3[23] == 1 and body_3[25] == 1:
        if body_3[16] ==1 and body_3[30] == 1:
            if body_3[9] ==1 and body_3[37] == 0:
                return 2
            if body_3[9] ==0 and body_3[37] == 1:
                return 1
            if body_3[9] ==1 and body_3[37] == 1:
                if body_3[2] ==1 and body_3[44] == 0:
                    return 2
                if body_3[2] ==0 and body_3[44] == 1:
                    return 1
                if body_3[2] ==1 and body_3[44] == 1:
                    return 2
    if body_3[25] == 1 and body_3[23] == 1:
        if body_3[18] ==1 and body_3[32] == 1:
            if body_3[11] ==1 and body_3[39] == 0:
                return 2
            if body_3[11] ==0 and body_3[39] == 1:
                return 1
            if body_3[11] ==1 and body_3[39] == 1:
                if body_3[4] ==1 and body_3[46] == 0:
                    return 2
                if body_3[4] ==0 and body_3[46] == 1:
                    return 1
                if body_3[4] ==1 and body_3[46] == 1:
                    return 2
    if body_3[31] == 1 and body_3[30] == 1 and body_3[32] == 1 and body_3[17] == 1:
        if body_3[29] == 1 and body_3[33] == 0:
            return 4
        if body_3[29] == 0 and body_3[33] == 1:
            return 3
        if body_3[29] == 1 and body_3[33] == 1:
            if body_3[28] == 1 and body_3[34] == 0:
                return 4
            if body_3[28] == 0 and body_3[34] == 1:
                return 3
            if body_3[28] == 0 and body_3[34] == 1:
                return 4   

    #To avoid the wall(rad==1)
    #don't be close to the wall
    if wall_3[3] == 1:
        if body_3[23] == 1:
            return 2
        if body_3[31] == 1:
            return MOVE[direc[move_2[random.randrange(23, 26, 2)]]]
        if body_3[25] == 1:
            return 2
    if wall_3[21] == 1:
        if body_3[17] == 1:
            return 4
        if body_3[31] == 1:
            return 4
        if body_3[25] == 1:
            return MOVE[direc[move_2[random.randrange(17, 32, 14)]]]
    if wall_3[45] == 1:
        if body_3[17] == 1:
            return MOVE[direc[move_2[random.randrange(23, 26, 2)]]]
        if body_3[23] == 1:
            return 1
        if body_3[25] == 1:
            return 1
    if wall_3[27] == 1:
        if body_3[17] == 1:
            return 3
        if body_3[23] == 1:
            return MOVE[direc[move_2[random.randrange(17, 32, 14)]]]
        if body_3[31] == 1:
            return 3
    
    #at the edge but not the corner
    if wall_3[17] == 1 and wall_3[23] == 0 and wall_3[25] == 0:   #upper bound
        if body_3[23] == 1:
            return 2
        if body_3[25] == 1:
            return 2
        if body_3[31] == 1:
            if body_3[23] == 1:
                return 4
            elif body_3[25] == 1:
                return 3
            else:
                return MOVE[direc[move_2[random.randrange(23, 26, 2)]]]
    if wall_3[23] == 1 and wall_3[17] == 0 and wall_3[31] == 0:   #left bound
        if body_3[31] == 1:
            return 4
        if body_3[17] == 1:
            return 4
        if body_3[25] == 1:
            if body_3[17] == 1:
                return 2
            elif body_3[31] == 1:
                return 1
            else:
                return MOVE[direc[move_2[random.randrange(17, 32, 14)]]]
    if wall_3[25] == 1 and wall_3[17] == 0 and wall_3[31] == 0:   #right bound
        if body_3[31] == 1:
            return 3
        if body_3[17] == 1:
            return 3
        if body_3[23] == 1:
            if body_3[17] == 1:
                return 2
            elif body_3[31] == 1:
                return 1
            else:
                return MOVE[direc[move_2[random.randrange(17, 32, 14)]]]
    if wall_3[31] == 1 and wall_3[23] == 0 and wall_3[25] == 0:   #lower bound
        if body_3[25] == 1:
            return 1
        if body_3[23] == 1:
            return 1
        if body_3[17] == 1:
            if body_3[23] == 1:
                return 4
            elif body_3[25] == 1:
                return 3
            else:
                return MOVE[direc[move_2[random.randrange(23, 26, 2)]]]
                
    #at the corner(rad=1)
    if wall_3[17] == 1 and wall_3[23] == 1:   #upper-left
        if body_3[25] == 1:
            return 2
        elif body_3[31] == 1:
            return 4
    if wall_3[31] == 1 and wall_3[23] == 1:   #lower-left
        if body_3[17] == 1:
            return 4
        elif body_3[25] == 1:
            return 1
    if wall_3[31] == 1 and wall_3[25] == 1:   #lower-right
        if body_3[17] == 1:
            return 3
        elif body_3[23] == 1:
            return 1
    if wall_3[17] == 1 and wall_3[25] == 1:   #upper-right
        if body_3[23] == 1:
            return 2
        elif body_3[31] == 1:
            return 3

    #we see the getfood(3),turn the direction to where the density is higher
        else:
            if food_3[2] == 1 or food_3[4] == 1:
                return 1
            if food_3[14] == 1 or food_3[28] == 1:
                return 3
            if food_3[44] == 1 or food_3[46] == 1:
                return 2
            if food_3[20] == 1 or food_3[34] == 1:
                return 14
    
    # view (radius = 1):
    # 00 01 02
    # 03 me 05
    # 06 07 08
        
    # view (radius = 2):
    # 00 01 02 03 04
    # 05 06 07 08 09
    # 10 11 me 13 14
    # 15 16 17 18 19
    # 20 21 22 23 24
    # Max radius is 3
    
    # view (radius = 3):
    # 00 01 02 03 04 05 06
    # 07 08 09 10 11 12 13
    # 14 15 16 17 18 19 20
    # 21 22 23 me 25 26 27
    # 28 29 30 31 32 33 34
    # 35 36 37 38 39 40 41
    # 42 43 44 45 46 47 48
    

f = open(sys.argv[1],'r')

print(actionToDo(1))
