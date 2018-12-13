'''
Created on 12 dec. 2018

@author: Ajayaha
got the concept help from https://www.youtube.com/watch?v=n5Ionw5LE18&t=914s
'''
import re

combination = {}
array = []


def readinput(fileName):
    global array
    with open(fileName, 'r') as filehandle:
        # array.append('.')
        line = filehandle.readline()
        # print(line)
        words = line.split(" ")
        # print()
        data = words[2].strip("\n")
        for c in data:
            array.append(c)
    
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
    start = 0
    zeroidx = 0
    strArray = 0
    print("[", "%2s" % year, "   ", "]", ''.join(array))
    tempArray = ''.join(array)
    for year in range(1, rotations + 1):
        if(year % 1000 == 0):
            print(year)
  
        strArray = "...." + tempArray + "...."
        zeroidx += 2
        
        del tempArray
        newarray = ''
        # print("[", "%2s" % year, zeroidx, "]", strArray)
        for i in range(0, len(strArray)):
            str = strArray[i:i + 5]
            if str in combination.keys():
                newarray += combination[str]
            else:
                newarray += '.'
                
        start = 0;
        end = len(newarray) - 1
        
        while newarray[start] == '.':
            start += 1
            zeroidx -= 1
            
        while newarray[end] == '.':
            end -= 1
        
        tempArray = newarray[start:end + 1]
        del newarray 
        print("[", "%2s" % year, zeroidx, "]", tempArray)
    zeroidx = -int(50e9) + 60   
    count = 0
    print(zeroidx)
    for i in range(len(tempArray)):
        if (tempArray[i] == '#'):
            count += (i - zeroidx)
    print(count)


def main():
    # readinput("example.txt")
    readinput("input.txt")
    # processData(20)
    processData(2000)

    
if __name__ == "__main__":
    main()
    
