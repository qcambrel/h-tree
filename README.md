## The Task

This is a programming exercise that I solved successfully on the Pramp platform in the past.

### The requirements were as follows:

I had to construct an H-tree given its center in x and y coordinates, starting length, and depth. A drawLine method was provided by the platform, so the actual act of drawing was abstracted out.

I was given an image of an H-tree similiar to [this](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/H_tree.svg/1200px-H_tree.svg.png) and an explanation of its structure.

Starting with a line segment of arbitrary length, I had to draw two segments of the equal length at right angles, with respect to the first line, through its endpoints, and then continuously performing the aforementioned while reducing, or dividing, the line segments at each stage by the square root of 2.

The drawLine method took four arguments: x0, x1, y0, and y1 respectively.

