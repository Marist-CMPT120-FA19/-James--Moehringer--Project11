from math import*


class Sphere:

    def __init__(self, radius):
        self.radius= radius
        self.surfacearea= (4*pi*(self.radius**2))
        self.volume= ((4/3)*pi*(self.radius**3))

    def getRadius(self):
        return self.radius

    def Surfacearea(self):
        return self.surfacearea

    def Volume(self):
        return self.volume

def main():

    radius= float(input("Please enter the radius of the sphere: "))
    getSphere= Sphere(radius)
    print("This sphere has a volume of: ", getSphere.Volume())
    print("This sphere has a surface area of: ", getSphere.Surfacearea())

main()
                  
