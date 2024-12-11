'''
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


def add (x,y,z):
    z=x+y+z
    return z
p=int(input("Enter 1st value")) 
q=int(input("Enter 2nd value"))
r=int(input("Enter 3rd value"))
x=add(p,q)
print(x)
# error ------>add() missing 1 required positional argument: 'z'

def add (x,y,z):
    z=x+y+z
    return z
p=int(input("Enter 1st value")) 
q=int(input("Enter 2nd value"))
r=int(input("Enter 3rd value"))
x=add(p,q,r,10)
print(x)
# error -----> add() takes 3 positional arguments but 4 were given
'''