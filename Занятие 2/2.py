  
import math
x = -4.5
y = 0.75*(10**-4)
z = -0.845*(10**2)
s = (((9+(((x-y))**2))**(1/3))/((x**2)+(y**2)+2))-(math.exp(abs(x-y)))*((math.tan(z))**3)
print(s)
