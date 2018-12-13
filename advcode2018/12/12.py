'''
Created on 12 dec. 2018

@author: Ajayaha
'''
import re

combination = {}
array = []


def readinput(fileName):
    global array
    with open(fileName, 'r') as filehandle:
        array.append('.')
        array.append('.')
        # array.append('.')
        line = filehandle.readline()
        # print(line)
        words = line.split(" ")
        # print()
        data = words[2].strip("\n")
        for c in data:
            array.append(c)
        
        array.append('.')
        array.append('.')
        array.append('.')

        # read empty line
        filehandle.readline()
        for line in filehandle:
            count = 0
            data = 0
            key = 0
            for word in line.split():
                if count == 0:
                    data = word
                if count == 2:
                    key = word
                count += 1
            combination.update([(data, key)])
        # print(input, len(input))
        # for (data, key) in combination.items():
        #    print(data, ":", key)


def processData(rotations):
    global array
    year = 0
    smart = 0
    print("[", "%2s" % year, "]", ''.join(array))
    for year in range(1, rotations + 1):
        if(year % 1000 == 0):
            print(year)
        
        newarray = []
        newarray.append('.',)
        newarray.append('.',)
        for i in range(1 + smart, len(array)):
            # print(input[i], end="")
            str = ''.join(array[i - 2:i + 3])
            # print(str, "-->", end="")
            if str in combination.keys():
                newarray.append(combination[str])
                # print(combination[str], ":" , ''.join(newarray))
            else:
                newarray.append('.',)
                # print(".", ":" , ''.join(newarray))
            # print(''.join(newarray))
        newarray.append('.',)
        print("[", "%2s" % year, "]", ''.join(newarray))
        array = newarray
    
    count = 0
    for i in range(rotations, len(array)):
        if (array[i] == '#'):
            count += (i - (rotations) - 2)
    print(count)


def main():
    # readinput("example.txt")
    readinput("input.txt")
    # print(input)
    processData(20)
    # processData(50000000000)

    
if __name__ == "__main__":
    main()
    
