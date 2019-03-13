class Node:
    """description of class"""
    def __init__(self, getLocation):
        self.location = getLocation
        self.leftChild = None
        self.righChild = None
        self.parentNode = None
        
    def setLeft(self, toLeft):
        toLeft.parentNode = self
        self.leftChild = toLeft

    def setRight(self, toRight):
        toRight.parentNode = self
        self.rightChild = toRight

    def goLeft(self):
        return self.leftChild

    def goRight(self):
        return self.rightChild

    def getLocation(self):
        if self.location != None:
            self.location.getInfo()
        else:
            print('This branch is empty')

    

