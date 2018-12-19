'''
Created on 13 dec. 2018

@author: Ajayaha
'''
from copy import deepcopy

input_1 = []
input_backup = []
wagenPos = []
input_2 = []
 

def printData(data):
    for a in data:
        print(''.join(a))


def prepareWagePos():
    lineNo = 0
    for line in input_1:
        charNo = 0
        for char in line:
            if ((char == '<') or (char == '>') or(char == 'v') or(char == '^')) :
                wagenPos.append((lineNo, charNo, char, "left"))
            charNo += 1
        lineNo += 1


def prepareBackup():
    global input_backup 
    input_backup = deepcopy(input_1)
    lineNo = 0
    for line in input_1:
        charNo = 0
        for char in line:
            if ((char == '<') or (char == '>') or(char == 'v') or(char == '^')) :
                wagenPos.append((lineNo, charNo, char, "left"))
            charNo += 1
        lineNo += 1
    
    for wagen in wagenPos:
        print(wagen)
        x = wagen[0] 
        y = wagen[1]
        c = wagen[2]
        
        if ((input_1[x][y - 1] == '-') and 
            (input_1[x][y + 1] == '-') and
            (input_1[x - 1] [y] == '|') and
            (input_1[x + 1] [y] == '|')):
            input_backup[x][y] = '+'
            
        elif((c == '>' or (c == '<'))and (input_1[x][y - 1] != ' ') and  (input_1[x][y + 1] != ' ')):
                input_backup[x][y] = '-'
                
        elif((c == 'v' or (c == '^'))and (input_1[x - 1][y] != ' ') and (input_1[x + 1][y] != ' ')):
                input_backup[x][y] = '|'
                
        elif((input_1[x - 1][y] != ' ') and (input_1[x][y - 1] != ' ')):  
            input_backup[x][y] = '/'
                
        elif((input_1[x][y + 1] != ' ') and (input_1[x - 1][y] != ' ')):
            input_backup[x][y] = '\\'
        
        elif((input_1[x][y - 1] != ' ') and (input_1[x + 1][y] != ' ')):
            input_backup[x][y] = '\\'
        
        elif((input_1[x][y + 1] != ' ') and (input_1[x - 1][y] != ' ')):
            input_backup[x][y] = '/'

        else:
            print(wagen)
            assert(0)
        print("input_backup")
    printData(input_1)
    printData(input_backup)


def readInput(filename):
    global input_backup
    with open(filename, 'r') as filehandle:
        linecount = 0
        
        for line in filehandle:
            line = line.strip('\n')
            input_1.append([])
            input_1[linecount].append(' ')
            for c in line:
                input_1[linecount].append(c)
            input_1[linecount].append(' ')
            linecount += 1
    
    dummy = []
    for _ in range(len(input_1[0])):
        dummy.append(' ')
    input_1.insert(0, dummy)
    prepareBackup()


def moveWagen(info):
    # find next position
    global input_backup
    global input_2
    c_x = info[0]
    c_y = info [1]
    c_c = info[2]
    c_dir = info[3]
    
    if (c_c == '>'):
        n_x = c_x
        n_y = c_y + 1
        n_dir = c_dir
        if(input_backup[c_x][c_y + 1] == '-'):
            n_c = c_c
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x][c_y + 1] == '\\'):
            n_c = 'v'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x][c_y + 1] == '/'):
            n_c = '^'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x][c_y + 1] == '+'):
            if(c_dir == 'left'):
                n_c = '^'
                n_dir = "stright"
                # return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'stright'):
                n_c = '>'
                n_dir = "right"
                # return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'right'):
                n_c = 'v'
                n_dir = "left"
                # return(n_x, n_y, n_c, n_dir)
            else:
                assert(1)
        else:
            print(info)
            assert(0)
        
        if(input_2[n_x][n_y] == '<' or
           input_2[n_x][n_y] == '>' or
           input_2[n_x][n_y] == 'v' or
           input_2[n_x][n_y] == '^'):
            print(info, (n_x, n_y, n_c, n_dir) , input_2[n_x][n_y])
            print("answer:", n_y - 1, n_x - 1)
            assert(0)
        return(n_x, n_y, n_c, n_dir)
            
    elif(c_c == '<'):
        n_x = c_x
        n_y = c_y - 1
        n_dir = c_dir
        if(input_backup[c_x][c_y - 1] == '-'):
            n_c = c_c
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x][c_y - 1] == '\\'):
            n_c = '^'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x][c_y - 1] == '/'):
            n_c = 'v'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x][c_y - 1] == '+'):
            if(c_dir == 'left'):
                n_c = 'v'
                n_dir = "stright"
                # return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'stright'):
                n_c = '<'
                n_dir = "right"
                # return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'right'):
                n_c = '^'
                n_dir = "left"
                # return(n_x, n_y, n_c, n_dir)
            else:
                assert(1)
        else:
            print(info)
            assert(0)
            
        if(input_2[n_x][n_y] == '<' or
           input_2[n_x][n_y] == '>' or
           input_2[n_x][n_y] == 'v' or
           input_2[n_x][n_y] == '^'):
            print(info, (n_x, n_y, n_c, n_dir) , input_2[n_x][n_y])
            print("answer:", n_y - 1, n_x - 1)
            assert(0)
        return(n_x, n_y, n_c, n_dir)            
    
    elif(c_c == 'v'):
        n_x = c_x + 1
        n_y = c_y 
        n_dir = c_dir
        if(input_backup[c_x + 1][c_y] == '|'):
            n_c = c_c
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x + 1][c_y] == '\\'):
            n_c = '>'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x + 1][c_y] == '/'):
            n_c = '<'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x + 1][c_y] == '+'):
            if(c_dir == 'left'):
                n_c = '>'
                n_dir = "stright"
                # return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'stright'):
                n_c = 'v'
                n_dir = "right"
                # return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'right'):
                n_c = '<'
                n_dir = "left"
                # return(n_x, n_y, n_c, n_dir)
            else:
                assert(0)
        else:
            print(info)
            assert(0)
        print(n_x, n_y, n_c, n_dir)
        if(input_2[n_x][n_y] == '<' or
           input_2[n_x][n_y] == '>' or
           input_2[n_x][n_y] == 'v' or
           input_2[n_x][n_y] == '^'):
            print(info, (n_x, n_y, n_c, n_dir) , input_2[n_x][n_y])
            print("answer:", n_y - 1, n_x - 1)
            assert(0)
        return(n_x, n_y, n_c, n_dir)

    elif(c_c == '^'):
        n_x = c_x - 1
        n_y = c_y 
        n_dir = c_dir
        if(input_backup[c_x - 1][c_y] == '|'):
            n_c = c_c
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x - 1][c_y] == '\\'):
            n_c = '<'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x - 1][c_y] == '/'):
            n_c = '>'
            # return(n_x, n_y, n_c, n_dir)
        elif(input_backup[c_x - 1][c_y] == '+'):
            if(c_dir == 'left'):
                n_c = '<'
                n_dir = "stright"
                # return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'stright'):
                n_c = '^'
                n_dir = "right"
                return(n_x, n_y, n_c, n_dir)
            elif(c_dir == 'right'):
                n_c = '>'
                n_dir = "left"
                # return(n_x, n_y, n_c, n_dir)
            else:
                assert(0)
        else:
            print(info)
            assert(0)
        
        if(input_2[n_x][n_y] == '<' or
           input_2[n_x][n_y] == '>' or
           input_2[n_x][n_y] == 'v' or
           input_2[n_x][n_y] == '^'):
            print(info, (n_x, n_y, n_c, n_dir) , input_2[n_x][n_y])
            print("answer:", n_y - 1, n_x - 1)
            assert(0)
        return(n_x, n_y, n_c, n_dir)


def processTicks():
    global wagenPos
    global input_1
    global input_2    
    temp_input = deepcopy(input_1)
    # 1)find the positions of "< > ^ v"
    
    # 2)move the positions one by one
    
    # 3)check for X if not repeat 2
    # for tmp in waganPos:
    #    print(tmp)
    # temp_inout = []
    for tick in range(20000):
        print(tick)
        input_1 = deepcopy(temp_input)
        input_2 = deepcopy(temp_input) 
        for wagenCount in range (0, len(wagenPos)):
            wagen = wagenPos[wagenCount]
            nextWagenPos = moveWagen(wagen)
            # print("samba-->", tick, wagenCount, wagen, nextWagenPos)
            temp_input[wagen[0]][wagen[1]] = input_backup[wagen[0]][wagen[1]]
            temp_input[nextWagenPos[0]][nextWagenPos[1]] = nextWagenPos[2]
            wagenPos[wagenCount] = nextWagenPos
            input_2 = deepcopy(temp_input) 
        # printData(temp_input)

        
def main():
    #
     
    # readInput("example1.txt")
    readInput("input.txt")
    processTicks()


if __name__ == "__main__":
    main()
