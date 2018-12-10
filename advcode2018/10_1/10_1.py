'''
Created on 10 dec. 2018

@author: Ajayaha
GOT INSPIRED FROM https://www.youtube.com/watch?v=0c_AkJK7Fhk
'''
import re
data = []


def readinput():
    count = 0
    global data 
    for line in open('input.txt', 'r'):
        x, y, vx, vy = re.findall('-?\d+', line)
        data.append([int(x), int(y), int(vx), int(vy)])
        # print(data[count])
        # count += 1


def printAndProcess():
    global data
    f = open("output.txt", "w")
    for t in range(0, 100000):
        xmin = min([x for x, _, _, _ in data])
        xmax = max([x for x, _, _, _ in data])
        ymin = min([y for _, y, _, _ in data])
        ymax = max([y for _, y, _, _ in data])
        print(xmin, xmax, ymin, ymax)
        W = 100
        if(((xmin + W) >= xmax) and ((ymin + W) >= ymax)):
            f.write(str(t))
            f.write(":") 
            f.write("\n") 
            for yval in range(ymin, ymax + 1):
                for xval in range(xmin, xmax + 1):
                    if(xval, yval) in [(x, y)  for x, y, _, _ in data]:
                        # print('#', end='')
                        f.write('#')
                    else:
                        # print('.', end='')
                        f.write('.')
                f.write("\n")
                f.write("\n")
                
        for dataelem in data:
             dataelem[0] = dataelem[0] + dataelem[2]
             dataelem[1] = dataelem[1] + dataelem[3]  

            
def main():
    readinput()
    printAndProcess()


if __name__ == "__main__":
    main()
