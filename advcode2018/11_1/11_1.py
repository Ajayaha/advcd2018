'''
Created on 11 dec. 2018

@author: Ajayaha
'''


def calcPower(x, y, serial):
    rackid = x + 10
    p1 = ((rackid * y + serial) * rackid) % 1000
    p = int(p1 / 100) - 5
    return(p)


def findResult(serial):
    maxval = -100000000
    for x in range(1, 299):
        for y in range(1, 299):
            val = 0
            for xval in range(0, 3):
                for yval in range(0, 3):
                    val += calcPower(x + xval, y + yval, serial)
            if(maxval < val):
                maxval = val
                pos = (x, y)
            else:
                pass
    print(maxval, pos)


def findResultSize(serial, size_val):
    maxval = -100000000
    size = 0
    pos = (0, 0)
    while size < size_val :
        print(size, ":", maxval, pos, size)
        for x in range(1, 300 - size):
            for y in range(1, 300 - size):
                val = 0
                for xval in range(0, size):
                    for yval in range(0, size):
                        if((x + xval < 299) and (y + yval < 299)):
                            val += calcPower(x + xval, y + yval, serial)
                if(maxval < val):
                    maxval = val
                    pos = (x, y)
                else:
                    pass
        size += 1
    print(maxval, pos, size)

    
def main():
    # print(calcPower(122, 79, 57))
    # print(calcPower(217, 196, 39))
    # print(calcPower(101, 153, 71))
#    findResult(18)
#   findResult(42)
    findResult(8444)
    # findResultSize(18, 16) 
    # findResultSize(42, 20)
    findResultSize(8444, 299)


if __name__ == "__main__":
    main()
