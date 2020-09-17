from asciiObj import AsciiObj

class Tree:
    SPACE = " "
    FG = "*"
    NEWLINE = "\n"
    """
    """
    def __init__(self, layers=7, widen = 1, margin=0, bg= SPACE):
        self.lines = []
        self.bg = bg
        self.layers = layers
        self.widen = widen
        self.margin = margin
        
        self.build (self.widen, self.bg)
        self.timesRotated = 0
        pass
    
    def line(self, x, n, fg=FG): 
        """return a string of n chararcters fg center at position x
        """
        singleLine = "" + (fg * n).center(2 * x + 1, self.bg)
        return singleLine
    
    def triangle (self, x, hw, fg=FG):
        
        """Return a list of strings that represent a trapezoid with 
            * x-coordinate centered at x
            * bottom width = 2*hw + 1
            * height = (hw+1)//2 + 1
            * top width    = (bottom width) - 2*(height) + 2
            * forground symbol = fg (default aterisk)""" 
        trapezoidLines = []
        height = (hw + 1) // 2 + 1
        startWidth = ((2 * hw) + 1) - (2 * height - 2)
        for i in range(0, height):
            trapezoidLines.append(self.line(x, startWidth + 2 * i, fg))
        return trapezoidLines

    def treeTop (self, x):
        """Return a list of strings that represents n-layered trapzoid of the tree
        """
        treeCanopy = []
        for i in range(0, self.layers + 1):
            treeCanopy.extend(self.triangle(x * self.widen, i * self.widen, str(i%10)))
        return treeCanopy

    def treeTrunk (self, x,hw):
        """Return a list of strings that represents the tree trunk with
            * width  = 2*hw+1
            * height = 2*width
        """
        trunkLines = []
        lilN = hw
        theWidth = ((lilN * self.widen) // 3) * 2 + 1
        for i in range(0, 2 * theWidth):
            trunkLines.append(self.line(x * self.widen,  theWidth, "T"))
        return trunkLines

    def build (self, widen=1, bg=SPACE):
        """Compose a list of lines that represent a n-layer tree with
            * the background symbol = bg  (default is the space character)
            * the tree width = 2*n*widen + 1 (widen defaults to 1)"""
        self.bg = bg
        self.lines = []
        self.widen = widen
        maxWidth = 2 * self.layers + 1
        mid = maxWidth // 2
        self.lines.extend(self.treeTop(mid))
        nThing = (self.layers // 3)
        self.lines.extend(self.treeTrunk(mid, self.layers))
        pass
    
    def  rotate (self):
        """Revise the list of strings self.lines that represents the tree rotated 45 degree clockwise
        """
        self.timesRotated += 1
        sideways = []
        for i in range(0, len(self.lines[0])):
            sidewayLine = ""
            for j in range(0, len(self.lines)):
                sidewayLine += self.lines[len(self.lines) - 1 - j][i]
            sideways.append(sidewayLine)
        self.lines = sideways

    # Revise the following function as follows:
    # 1. add new parameter border with default 0
    # 2. change the default of bg to None
    def draw (self, reverse=False, bg=None, margin=0, border=0):
        self.reverse = reverse
        #self.bg = bg
        self.margin = margin
        self.border = border
        """
        if (bg != self.bg):
            self.bg = bg
            self.build(widen = self.widen, bg = self.bg)
            for i in range(0, self.timesRotated):
                self.rotate()
        """
        oldBg = self.bg
        self.bg = bg
        newBg = self.bg
        if (bg != None):
            for i, v in enumerate(self.lines):
                nouveau = v.replace(oldBg, newBg)
                self.lines[i] = nouveau
        
        """Print out the list of strings that represents the tree with
            * background symbol=bg (default None )
            * the number of spaces to the left screen border = margin (default 0)
            * If border=n > 0, then replace the n layers of the tree border with special symbols.
            * If reverse=True, the tree will be printed out upside down """
        AsciiObj.drawLines(self.lines, self.bg, self.reverse, self.margin, self.border)
        pass
