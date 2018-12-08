'''
Created on 8 dec. 2018

@author: Ajayaha
'''

from sys import setrecursionlimit
import threading

inputList = []
index = 0
keyVal = 1;
sumOfMeta = 0

setrecursionlimit(100000)


def readinput():
    # fileHandle = open('input.txt', 'r')
    with open('input.txt', 'r') as f:
        for line in f:
            for word in line.split():
                inputList.append(int(word))
    
    
class Node(object):

    def __init__(self):
        global keyVal
        # print(keyVal)
        self.m_noOfChildren = None
        self.m_noOfMetadata = None
        self.m_key = keyVal
        keyVal += 1
        # deleted because of size
        # self.m_listOfChild = []
        # self.m_listOfMeta = []
        
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

    '''
    def getListOfMetadata(self): 
       return (self.m_listOfMeta)
    
    def getListOfChildren(self): 
        return (self.m_listOfChild)
    '''

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
         #   nodeTree.getListOfMetadata().append(inputList[index])
            sumOfMeta += inputList[index]
            # print(sumOfMeta, inputList[index], self.getKey())
            index += 1
            # work after call


readinput()
nodeTree = Node()
nodeTree.insertNode()
print(sumOfMeta)
