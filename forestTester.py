from forest import Forest
from tree import Tree

def test1():
    tree = Tree(widen=2, layers = 7) # construct a 7-layer tree with 2x default width
    for i in range (4):
        tree.draw(margin = 30, bg = ".", border=2)
        tree.rotate()
    pass

def test2():
    f = Forest([5,2,3,7] )  # a forest of tree with layers = 5,2,3, and 7 as shown below
    f.draw()
    pass

def test3():
    f = Forest([5,2,3,7], widen=2, margin=10 )  #
    f.draw()
    pass

def test4():
    f = Forest([5,2,3,7], widen=2, margin=10 )  #
    f.rotate() #
    f.draw(bg=".")
    pass

def test5():
    f = Forest([11,5, 9,7]) 
    f.rotate(1 ) #
    for i in range (3):
        f.rotate( 2 ) #
    f.draw(bg=" ")
    pass
