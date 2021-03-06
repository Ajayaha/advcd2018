'''
Created on 8 dec. 2018

@author: Ajayaha
'''

inputList = []
index = 0
keyVal = 1;
sumOfMeta = 0


def readinput():
    with open('input.txt', 'r') as f:
        for line in f:
            for word in line.split():
                inputList.append(int(word))
    
    
class Node(object):

    def __init__(self):
        global keyVal
        self.m_noOfChildren = None
        self.m_noOfMetadata = None
        self.m_key = keyVal
        keyVal += 1
        
    def getKey(self): 
        return self.m_key
    
    def setNoOfChildren(self, obj): 
        self.m_noOfChildren = obj

    def getNoOfChildren(self): 
        return (self.m_noOfChildren)
    
    def setNoOfMetadata(self, obj): 
        self.m_noOfMetadata = obj

    def getNoOfMetadata(self): 
        return (self.m_noOfMetadata)

    def insertNode(self):
        global keyVal
        global index
        global sumOfMeta
        self.setNoOfChildren(inputList[index])
        index += 1
        self.setNoOfMetadata(inputList[index])
        index += 1
        # termination condition
        for i in range(0, self.getNoOfChildren()):
            # work before call
            node = Node()
            # recursive call
            node.insertNode()
        for j in range (0, self.getNoOfMetadata()):
            sumOfMeta += inputList[index]
            index += 1
            # work after call


readinput()
nodeTree = Node()
nodeTree.insertNode()
print(sumOfMeta)
