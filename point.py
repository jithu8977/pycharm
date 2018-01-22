import math
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dist=math.sqrt(dx**2+dy**2)
    print("dist is",dist)

distance(5,4,2,3)
