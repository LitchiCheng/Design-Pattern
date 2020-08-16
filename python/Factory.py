class Shape:
    def draw(self):
        pass

class Triangle(Shape):
    def draw(self):
        print("i am triangle")

class Circle(Shape):
    def draw(self):
        print("i am circle")

class Factory:
    def __init__(self):
        self._shape = Shape()
    def getShape(self, type):
        if type == "triangle":
            self._shape = Triangle()
            return self._shape
        elif type == "circle":
            self._shape = Circle()
            return self._shape
    
if __name__ == "__main__":
    factory = Factory()
    factory.getShape("circle").draw()
    factory.getShape("triangle").draw()