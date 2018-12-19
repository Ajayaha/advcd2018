'''
Created on 19 dec. 2018

@author: Ajayaha
'''
import re
from manhattandist.manhattandist import fileHandle

input 
inst = []
output = []
result = []
dict = {}


def printdata(dicta):
    for i in dicta:
        print(i, ": ", end='')
        print(list(set(dict[i])))


def funcAddr():
    if(input[inst[1]] + input[inst[2]] == output[inst[3]]):
        dict[inst[0]].append("addr")
        result.append("addr")


def funcAddi():
    if(input[inst[1]] + inst[2] == output[inst[3]]):
        dict[inst[0]].append("addi")
        result.append("addi")


def funcMulr():
    if(input[inst[1]] * input[inst[2]] == output[inst[3]]):
        dict[inst[0]].append("mulr")
        result.append("mulr")


def funcMuli():
    if(input[inst[1]] * inst[2] == output[inst[3]]):
        dict[inst[0]].append("muli")
        result.append("muli")


def funcBanr():
    if(input[inst[1]] & input[inst[2]] == output[inst[3]]):
        dict[inst[0]].append("banr")
        result.append("banr")


def funcBani():
    if(input[inst[1]] & inst[2] == output[inst[3]]):
        dict[inst[0]].append("bani")
        result.append("bani")

        
def funcBorr():
    if(input[inst[1]] | input[inst[2]] == output[inst[3]]):
        dict[inst[0]].append("borr")
        result.append("borr")


def funcBori():
    if(input[inst[1]] | inst[2] == output[inst[3]]):
        dict[inst[0]].append("bori")
        result.append("bori")

        
def funcSetr():
    if(input[inst[1]] == output[inst[3]]):
        dict[inst[0]].append("setr")
        result.append("setr")

                
def funcSeti():
    if(inst[1] == output[inst[3]]):
        dict[inst[0]].append("seti")
        result.append("seti")

        
def funcGtir():
    if(inst[1] > input[inst[2]]):
        if(output[inst[3]] == 1):
            dict[inst[0]].append("gtir")
            result.append("gtir")
        
    else: 
        if(output[inst[3]] == 0):
            dict[inst[0]].append("gtir")
            result.append("gtir")


def funcGtri():
    if(input[inst[1]] > inst[2]):
        if(output[inst[3]] == 1):
            dict[inst[0]].append("gtri")
            result.append("gtri")
    else: 
        if(output[inst[3]] == 0):
            dict[inst[0]].append("gtri")
            result.append("gtri")


def funcGtrr():
    if(input[inst[1]] > input[inst[2]]):
        if(output[inst[3]] == 1):
            dict[inst[0]].append("gtrr")
            result.append("gtrr")
        
    else: 
        if(output[inst[3]] == 0):
            dict[inst[0]].append("gtrr")
            result.append("gtrr")


def funcEqir():
    if(inst[1] == input[inst[2]]):
        if(output[inst[3]] == 1):
            dict[inst[0]].append("eqir")
            result.append("eqir")
        
    else: 
        if(output[inst[3]] == 0):
            dict[inst[0]].append("eqir")
            result.append("eqir")


def funcEqri():
    if(input[inst[1]] == inst[2]):
        if (output[inst[3]] == 1):
            dict[inst[0]].append("eqri")
            result.append("eqri")
        
    else: 
        if(output[inst[3]] == 0):
            dict[inst[0]].append("eqri")
            result.append("eqri")


def funcEqrr():
    if(input[inst[1]] == input[inst[2]]):
        if(output[inst[3]] == 1):
            dict[inst[0]].append("eqrr")
            result.append("eqrr")
        
    else: 
        if(output[inst[3]] == 0):
            dict[inst[0]].append("eqrr")
            result.append("eqrr")


def executepart1(filename):
    global input 
    global inst 
    global output 
    global dict
    global result
    count = 0
    
    with open(filename, 'r') as filehandle:
        
        for line in filehandle:
            input = []
            inst = []
            output = []
            result = []
            
            data = (re.findall('-?\d+', line))
            for d in data:
                input.append(int(d))
            
            line = filehandle.readline()
            data = (re.findall('-?\d+', line))
            for d in data:
                inst.append(int(d))
            
            line = filehandle.readline()
            data = (re.findall('-?\d+', line))
            for d in data:
                output.append(int(d))
            
            line = filehandle.readline()
            
            funcAddr()
            funcAddi()
            
            funcMulr()
            funcMuli()

            funcBanr()
            funcBani()
            
            funcBorr()
            funcBori()
            
            funcSetr()
            funcSeti()
            
            funcGtir()
            funcGtri()
            funcGtrr()

            funcEqir()
            funcEqri()
            funcEqrr()
            
            if(len(result) >= 3):
                count += 1
            
        print(count)
    
    
def sortdict():
    opcode = {}
    for i in range(16):
        opcode[i] = []
        
    for i in range(16):
        dict[i] = list(set(dict[i]))

    for _ in range(16):
        for i in range(16):
            if(len(dict[i]) == 1):
                delvalue = dict[i][0]
                for j in range(16):
                    if(len(dict[j]) > 1):
                        for k in range(len(dict[j])):
                            if(dict[j][k] == delvalue):
                                dict[j] = dict[j][0:k] + dict[j][k + 1:len(dict[j])]
                                break;
    printdata(dict)
        

def main():
    global dict
    # readInput("input.txt")
    for i in range(16):
        dict[i] = []
    # readInput("sample.txt")
    executepart1("input.txt")
    
    sortdict()


if __name__ == "__main__":
    main()
