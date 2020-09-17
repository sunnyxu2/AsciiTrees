class AsciiObj:
    SPACE = " "          # the default space character
        
    @staticmethod        
    def addBorder(lines, bg=None, k=1):
        """The is a static method 
            * The input argument lines represent objects with background symbol bg
            * If k > 0, then it replace k-layer border with symbol "@" around the object represented in lines
            * This is a helper function for drawLines
        """
        if bg == None or k <=0:
            return 
        m = len ( lines)
        n = len (lines[0])
        mark = "@"
        for i,s in enumerate (lines): # for row s=lines[i]
            s2 = ""
            for j, x in enumerate (s):  # for character x=s[j]
                if x != bg:             # if the current character x is not background symbol
                    if  (i<=k or i>=m-k or j<=k or j>=n-k):   
                        # check if x is within the k layers of the screen borders  (left,right, top, bottom)
                        x = mark         # replace x with special symbol if yes                     
                    elif lines[i-k][j]==bg or lines[i+k][j]==bg or s[j-k] == bg or s[j+k] ==bg:
                        # check if x is within the k layers of the tree object border (left,right, top, bottom)
                        x = mark         # # replace x with special symbol if yes
                s2 += x
            lines[i] = s2
    @staticmethod        
    def  rotate90 (lines):
        """Rotate the object represented by "lines" 90 degree clockwise
        * This is a static method to be shared with class Tree, Forest

        """
        m = len (lines)
        n = len (lines[0])
        ans = []
        for i in range (n):
            x=""
            for s in lines[::-1]:
                x += s[i]
            ans.append (x)
        return ans

    @staticmethod        
    def drawLines (lines, bg=None, reverse=False, margin=0, border=0): 
        """* Print out lines with 
            * the number of spaces to the left screen border = margin (default 0)
            * If border=n > 0, then replace the n layers of the object borders with special symbol @.
            * If reverse=True, the objects will be printed out upside down
            * This is a static method to be used by both class Tree and class Forest
        """           
        if reverse:
            lines.reverse() 

        if border > 0 :
            AsciiObj.addBorder (lines, bg, border)

        offset = " " * margin
        for s in lines:
            print (offset+s)
