from tree import Tree

def test1():
    tree = Tree(layers=7)
    tree.draw()
    pass

def test2():
    tree = Tree(layers=7) 
    tree.draw( margin = 30 )
    pass

def test3():
    tree = Tree(7) 
    tree.draw( reverse=True)
    pass

def test4():
    tree = Tree()
    tree.build(widen=2)
    tree.draw()
    pass

def test5():
    tree = Tree(widen=2, layers = 7) 
    tree.draw(margin = 30, bg = ".")
    pass

def test6():
    tree = Tree(7) 
    tree.draw() 
    for i in range (4):
        tree.rotate()
        tree.draw() 
    pass
