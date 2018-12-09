'''
Created on 8 dec. 2018

@author: Ajayaha
'''

inputList = []
index = 0
keyVal = 1;


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
        self.m_value = 0
        self.m_arrayOfValues = []
        self.m_listOfMeta = []
    
    def setNoOfChildren(self, obj): 
        self.m_noOfChildren = obj

    def getNoOfChildren(self): 
        return (self.m_noOfChildren)
    
    def setNoOfMetadata(self, obj): 
        self.m_noOfMetadata = obj

    def getNoOfMetadata(self): 
        return (self.m_noOfMetadata)
    
    def getListOfMetadata(self): 
        return (self.m_listOfMeta)
    
    def getarrayOfValues(self): 
        return (self.m_arrayOfValues)

    def getValueOfRootNode(self):
        global keyVal
        global index
        self.setNoOfChildren(inputList[index])
        index += 1
        self.setNoOfMetadata(inputList[index])
        index += 1
        # termination condition
        for i in range(0, self.getNoOfChildren()):
            # work before call
            node = Node()
            # recursive call
            self.getarrayOfValues().append(node.getValueOfRootNode())
        
        for j in range (0, self.getNoOfMetadata()):
            self.getListOfMetadata().append(inputList[index])
            index += 1
        # work after call
        self.calculateValue()
        return(self.m_value)

    def calculateValue(self):
        if self.getNoOfChildren() == 0:
            for count in range(0, self.getNoOfMetadata()):
                self.m_value += self.getListOfMetadata()[count]
        else:
            for count in range(0, len(self.getListOfMetadata())):
                # add if  it is present
                # skip it is not present
                if(self.getListOfMetadata()[count] <= len(self.getarrayOfValues())):
                    self.m_value += self.getarrayOfValues()[self.getListOfMetadata()[count] - 1]

        
readinput()
nodeTree = Node()
nodeTree.getValueOfRootNode()
print(nodeTree.m_value)
