'''
Created on 14 dec. 2018

@author: Ajayaha
'''


def processData(rotations):
    s = [3, 7]
    a = 0
    b = 1
    for _ in range(rotations + 5):
        sum = s[a] + s[b]
        if sum >= 10:
            s.append(int(sum / 10)) 
            s.append(sum % 10) 
        else:
            s.append(sum % 10)
        a = (a + s[a] + 1) % len(s)
        b = (b + s[b] + 1) % len(s)
    
    data = ''
    
    for i in s[rotations:rotations + 10]:
        data += str(i)
    print(data)
    return data 


def main():
    if ("5158916779" == processData(9)):
        print("9 : passed")
    else:
        print("9 : Failed")
        
    if ("9251071085" == processData(18)):
        print("18 : passed")
    else:
        print("18 : Failed")
        
    if ("5941429882" == processData(2018)):
        print("2018: passed")
    else:
        print("2018 : Failed")

    processData(637061)  # test input


if __name__ == "__main__":
    main()
