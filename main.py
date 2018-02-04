# The "H-Tree Construction" Problem

def drawHTree(x,y,starting_length,depth):
   if depth = 0:
      return
   x0 = x - (starting_length / 2)
   x1 = x + (starting_length / 2)
   y0 = y - (starting_length / 2)
   y1 = y + (starting_length / 2)
   drawLine(x0, x1, y, y)     # normal line
   drawLine(x0, x0, y0, y1)   # parallel line
   drawLine(x1, x1, y0, y1)   # parallel line
   drawHTree(x0, y0, starting_length / sqrt(2), depth - 1)  # lower left  H-tree
   drawHTree(x0, y1, starting_length / sqrt(2), depth - 1)  # upper left  H-tree
   drawHTree(x1, y1, starting_length / sqrt(2), depth - 1)  # upper right H-tree
   drawHTree(x1, y0, starting_length / sqrt(2), depth - 1)  # lower right H-tree