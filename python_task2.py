#create class 
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

#display the point
    def display(self,x,y):
        print(f"Point: ({self.x}, {self.y})")

#after moving points
    def move(self,dx,dy):
            self.x = dx
            self.y = dy
            print(f"After move: ({self.x}, {self.y})")

#distance from origin
    def distance_from_origin(self,x,y):
        distance=math.sqrt(self.x**2+self.y**2)
        distance=round(distance,2)
        print(f"distance from origin:",distance)
        
#object creation
p=Point(4,6)
p.display(4,6)
p.move(7,8)
p.distance_from_origin(0,0)
