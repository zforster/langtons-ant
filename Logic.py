import random, pygame
from Ant import Ant

class Logic():
    def __init__(self,winWidth,winHeight,antSize,display):
        self.display = display
        self.antSize = antSize
        self.width = winWidth
        self.height = winHeight
        self.gridWidth = int(winWidth / antSize)
        self.gridHeight = int(winHeight / antSize)
        self.antList = []
        self.grid = self.generateGrid(self.gridWidth,self.gridHeight,[])
        self.spawnAnt(self.gridWidth,self.gridHeight,self.generateGrid(self.gridWidth,self.gridHeight,[]))
            
    def generateGrid(self,gridWidth, gridHeight, grid):
        for x in range(0,gridWidth):
            grid.append([])
            for y in range(0,gridHeight):
                grid[x].append(0)
        return grid
    
    def spawnAnt(self,gridWidth,gridHeight,grid):
        for i in range(0,200):
            xPos = random.randint(0,gridWidth-1)
            yPos = random.randint(0,gridHeight-1)
            ant = Ant()
            ant.setPos(xPos,yPos)
            self.antList.append(ant)
    
    def drawAnt(self,width,height,ant):
        pygame.draw.rect(self.display,(ant.getColour()),(width * self.antSize,height * self.antSize,self.antSize,self.antSize))
    
    def drawTrace(self,width,height,colour,ant):
        pygame.draw.rect(self.display,colour,(width * self.antSize,height * self.antSize,self.antSize,self.antSize))
        
    def draw(self,width,height,antWidth,antHeight,colour,ant):
        self.drawAnt(antWidth,antHeight,ant)
        self.drawTrace(width,height,colour,ant)
    
    def makeChange(self,direction,ant,width,height,antWidth,antHeight,val):
        ant.setDir(direction)
        ant.setPos(antWidth,antHeight)
        self.grid[width][height] = val
        
    
    def run(self):
        for ant in self.antList:
            width, height = ant.getPos()
            if(not(width > self.gridWidth - 1 or width < 0 or height > self.gridHeight - 1 or height < 0)):
                if(ant.getDir() == "north"):
                    if(self.grid[width][height] == 0):
                        self.makeChange("east",ant,width,height,width,height+1,1)
                        self.draw(width,height,width,height + 1,ant.getColour(),ant)
                    elif(self.grid[width][height] == 1):
                        self.makeChange("west",ant,width,height,width,height-1,0)
                        self.draw(width,height,width,height - 1,(0,0,0),ant)
                elif(ant.getDir() == "south"):
                    if(self.grid[width][height] == 0):
                        self.makeChange("west",ant,width,height,width,height-1,1)
                        self.draw(width,height,width,height - 1,ant.getColour(),ant)
                    elif(self.grid[width][height] == 1):
                        self.makeChange("east",ant,width,height,width,height+1,0)
                        self.draw(width,height,width,height + 1,(0,0,0),ant)
                elif(ant.getDir() == "east"):
                    if(self.grid[width][height] == 0):
                        self.makeChange("south",ant,width,height,width+1,height,1)
                        self.draw(width,height,width + 1,height,ant.getColour(),ant)
                    elif(self.grid[width][height] == 1):
                        self.makeChange("north",ant,width,height,width-1,height,0)
                        self.draw(width,height,width - 1,height,(0,0,0),ant)
                elif(ant.getDir() == "west"):
                    if(self.grid[width][height] == 0):
                        self.makeChange("north",ant,width,height,width-1,height,1)
                        self.draw(width,height,width - 1,height,ant.getColour(),ant)
                    elif(self.grid[width][height] == 1):
                        self.makeChange("south",ant,width,height,width+1,height,0)
                        self.draw(width,height,width-1,height,(0,0,0),ant)
        
            