"""
    Description: This program draws a design recursively in four corners, 
    getting progressively smaller.
    Author: Bhadra
    Date: September 2021
"""
from graphics import *

def drawDesign(win, beginPt, size):
    """
    Purpose: Draws design
    Parameters:  graphics window, point to draw design at, size of design
    Return Val:  points at four corners (diagonal)
    """
    width = win.getWidth()
    height = win.getHeight()

    #size is inverted (bigger number means smaller size)
    boxWidth = width/(15*size)
    boxHeight = height*2/(10*size)
    
    blX = beginPt.x - boxWidth*0.5
    blY = beginPt.y + boxHeight*0.5
    blCorner = Point(blX, blY)

    circleRadius = boxWidth
    circle1 = Circle(Point(blX + boxWidth, blY - boxHeight + circleRadius), circleRadius)
    circle2 = Circle(Point(blX, blY - circleRadius), circleRadius)

    circle1.draw(win)
    circle1.setFill("midnight blue")
    circle1.setOutline("midnight blue")

    circle2.draw(win)
    circle2.setFill("royal blue")
    circle2.setOutline("royal blue")

    box = Rectangle(blCorner, Point(boxWidth + blX, blY - boxHeight))
    box.draw(win)
    box.setFill("lightblue")
    box.setOutline("lightblue")

    midBlY = blY - (boxHeight/2) + boxWidth/2
    midBlCorner = Point(blX, midBlY)
    midBox = Rectangle(midBlCorner, Point(blX + boxWidth, midBlY - boxWidth))
    midBox.draw(win)
    midBox.setFill("saddle brown")
    midBox.setOutline("saddle brown")

    #purposefully creates diagonal pattern
    #bl
    p1 = blCorner.clone()
    p1.move(-boxWidth*2, boxWidth*3 - boxHeight/2)

    #br
    p2 = blCorner.clone()
    p2.move(boxWidth*3, boxWidth*2 - boxHeight/2)

    #tl
    p3 = blCorner.clone()
    p3.move(-boxWidth*2, -2*boxHeight + boxWidth*2)

    #tr
    p4 = blCorner.clone()
    p4.move(boxWidth*3, -2*boxHeight + boxWidth)

    return p1, p2, p3, p4
    

def recurseDesign(win, beginPts, beginSize, numRecurse):
    """
    Purpose: Draws the design recursively
    Parameters:  graphics window, points of corners to draw design, beginning size,
    number of times to recurse
    Return Val:  none (just draws output)
    """
    p1 = beginPts[0]
    p2 = beginPts[1]
    p3 = beginPts[2]
    p4 = beginPts[3]

    newSize = beginSize*2.2

    bl = drawDesign(win, p1, newSize)
    br = drawDesign(win, p2, newSize)
    tl = drawDesign(win, p3, newSize)
    tr = drawDesign(win, p4, newSize)

    if numRecurse > 1:
        recurseDesign(win, bl, newSize, numRecurse-1)
        
        recurseDesign(win, br, newSize, numRecurse-1)
        
        recurseDesign(win, tl, newSize, numRecurse-1)
        
        recurseDesign(win, tr, newSize, numRecurse-1)

def main():
    width = 600
    height = 600
    
    win = GraphWin("not paypal logo i promise with recursion", width, height)
   
    win.setBackground("blanched almond")

    width = win.getWidth()
    height = win.getHeight()

    size = 0.9

    beginPt = Point(width/2, height/2)

    beginPts = drawDesign(win, beginPt, size)

    recurseDesign(win, beginPts, size, 5)

    click = win.getMouse()

main()