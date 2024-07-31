#Surface Area & Volume of a Cylinder
import math
def Cylinder(radius,height):
    area = 2*math.pi*radius*(radius+height)
    volume = math.pi*radius**2*height
    return area,volume
    
radius = float(input('Enter The Radius Of The Cylinder.'))
height = float(input('Enter The Height Of The Cylinder.'))

area,volume = Cylinder(radius,height)

print(f'Surface Area Of the Cylinder: {area}')
print(f'Volume Of The cylinder: {volume}')