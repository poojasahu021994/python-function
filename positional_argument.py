# Positional argument
def add (x,y,z):
    z=x+y+z
    # print(z) ----->iske sath me None likha aata h
    return z
p=int(input("Enter 1st value")) 
q=int(input("Enter 2nd value"))
r=int(input("Enter 3rd value"))
x=add(p,q,r)
print(x)