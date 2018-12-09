'''
Created on 9 dec. 2018

@author: Ajayaha
'''
from _collections import defaultdict


def calculateMaxScore(players, marbles_val):
    print(players, marbles_val, "-->", end='')
    score = defaultdict(int)
    marbles = [0]
    current = 0
    for m in range(1, marbles_val):
        if(m % 10000 == 0):
            print(m)
        if(m % 23 == 0):
            current = (current - 7) % len(marbles)
            score[(m % players)] += m + marbles[current]  
            
            del marbles[current]
        
        else:
            current = (current + 2) % len(marbles)
            marbles.insert(current, m) 
    # print(score)
    print(max(score.values()))
    return(max(score.values()))


def readinput():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if(count == 0):
                    players = int(word)
                if(count == 6):
                    marbles_val = int(word)
                    return(players, marbles_val)
                count += 1
                

def main():
    
    if(calculateMaxScore(9, 25) == 32):
        print("Testcase1 passed")
    else:
        print("Testcase1 Failed")
        
    if(calculateMaxScore(10, 1618) == 8317):
        print("Testcase2 passed")
    else:
        print("Testcase2 Failed")
    
    if(calculateMaxScore(13, 7999) == 146373):
        print("Testcase3 passed")
    else:
        print("Testcase3 Failed")
    
    '''if(calculateMaxScore(17, 1104) == 2764):
        print("Testcase4 passed")
    else:
        print("Testcase4 Failed")
    '''
    if(calculateMaxScore(21, 6111) == 54718):
        print("Testcase5 passed")
    else:
        print("Testcase5 Failed")
    
    if(calculateMaxScore(30, 5807) == 37305):
        print("Testcase6 passed")
    else:
        print("Testcase6 Failed")           
    (players, marbles_val) = readinput()
    calculateMaxScore(players, marbles_val)

    
if __name__ == "__main__":
    main()

