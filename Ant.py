import random

class Ant():
    def __init__(self):
        self.rand = random.random()
        self.direction = "north"
        self.width = 0;
        self.height = 0;
        self.red = random.randint(1,254)
        self.green = random.randint(1,254)
        self.blue = random.randint(1,254)
        self.colour = (self.red,self.green,self.blue)
        if(self.rand <= 0.25):
            self.direction = "north";
        elif(self.rand > 0.25 and self.rand <= 0.5):
            self.direction = "south";
        elif(self.rand > 0.5 and self.rand <= 0.75):
            self.direction = "east";
        elif(self.rand > 0.75 and self.rand <= 1):
            self.direction = "west";
    
    def setPos(self,width,height):
        self.width = width
        self.height = height
    
    def getPos(self):
        return self.width, self.height
    
    def getDir(self):
        return self.direction
    
    def setDir(self,direction):
        self.direction = direction
    
    def getColour(self):
        return self.colour