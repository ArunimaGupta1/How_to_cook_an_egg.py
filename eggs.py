import math
print("Enter the properities of the egg with a space in between,1.Mass,2.Density,3.Specific Heat Capacity,4.Thermal Conductivity")
e=input()
m,p,c,k=map(float,e.split())
print("Enter the temperature (in C degrees) of the boiling water in which the egg is boiled")
Tw=float(input())
print("Enter the original temperature (in C degrees) of the egg before being put in the water")
To=float(input())

def compute(m,p,c,k,Tw,To):
    Ty=70
    l=((m**(2/3))*c*(p**(1/3)))/(k*((math.pi)**2)*(((4*math.pi)/3)**(2/3)))
    t=l*math.log(0.76*((To-Tw)/(Ty-Tw)))
    return t

print(compute(m,p,c,k,Tw,To))
