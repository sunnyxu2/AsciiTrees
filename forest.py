import functools
from asciiObj import AsciiObj
from tree import Tree

class Forest():

    def __init__ (self, ntree = [3,7,1,9], widen=1, margin=0, bg=Tree.SPACE):
        """Constructor:
            * self.lines is a list of strings use to draw a forest in ASCII
        """
        self.lines = []
        self.treeObjects = []
        self.widen = widen
        self.margin = margin
        self.bg = bg
        self.globalRot = 0
        for i, v in enumerate(ntree):
            self.treeObjects.append(Tree(v, self.widen, self.margin, self.bg))

        self.setLines()
        pass

    def setLines(self): # you may or may not implement this funcition
        """Compose a list of strings that represents the forest by combining the strings that 
            represent each individual tree.
           This is a helper function for build and rotate """
        treeDims = []
        for i, v in enumerate(self.treeObjects):
            treeDimPair = [0, 0] # first index is height and 2nd index is width
            treeDimPair[0] = len(v.lines)
            treeDimPair[1] = len(v.lines[0])
            treeDims.append(treeDimPair)
            
        maxHeight = functools.reduce(lambda a, b: a if (a[0] > b[0]) else b, treeDims)[0]

        treeIntermediary = []
        for i, v in enumerate(self.treeObjects):
            treeWithAir = []
            airHeight = maxHeight - treeDims[i][0]
            #print(airHeight)
            for j in range(0, airHeight):
                theAir = "" + self.bg*treeDims[i][1]
                treeWithAir.append(theAir)
            treeWithAir += v.lines
            treeIntermediary.append(treeWithAir)

        forestLinesNew = []
        for i in range(0, maxHeight):
            tempLine = ""
            tempMargin = self.bg * self.margin
            for j, v in enumerate(treeIntermediary):
                tempLine += treeIntermediary[j][i] + tempMargin
            forestLinesNew.append(tempLine)

        self.lines = forestLinesNew
        pass
            
            
    # Note: Change the default of bg to None   
    def draw(self, reverse=False, bg=None, margin = 0, border=0 ):
        """Print out the list of strings that represents the forest with
            * background symbol=bg --> default was changed to None
            * the number of spaces to the left boarder of the window = margin (default 0)
           If reverse=True, the forest will be printed out upside down 
           If border>0, then the border of the objects will be replaced with the special symbols. 
        """
        self.reverse = reverse
        self.margin = margin
        self.border = border
        oldBg = self.bg
        self.bg = bg
        newBg = self.bg
        if (bg != None):
            for i, v in enumerate(self.lines):
                nouveau = v.replace(oldBg, newBg)
                self.lines[i] = nouveau
        AsciiObj.drawLines(self.lines, newBg, self.reverse, self.margin, self.border)
        pass
           
    def  rotate (self, individual_rotation=None):
        """Revise the list of strings self.lines that represents the rotated trees.
            if individual_rotation=k is specified, then tree k is rotated 90 degree clockwise individually.
            If individual_rotation=None, then the entire forest will be rotated 90 degree clockwise.
        """
        if (individual_rotation == None):
            self.globalRot += 1
            sideways = []
            for i in range(0, len(self.lines[0])):
                sidewayLine = ""
                for j in range(0, len(self.lines)):
                    sidewayLine += self.lines[len(self.lines) - 1 - j][i]
                sideways.append(sidewayLine)
            self.lines = sideways
        else:
            if (not (individual_rotation >= len(self.treeObjects) or individual_rotation < 0)):
                self.treeObjects[individual_rotation].rotate()
            self.setLines()
        pass
