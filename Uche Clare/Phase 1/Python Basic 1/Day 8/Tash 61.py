#convert the distance (in feet) to inches, yards, and miles.
x=float(input('Distance in feet: '))
print('Converting feet to inches: ')
x1= (x*12)
print(x1)
print('Converting feet to miles: ')
x2= (x/5280)
print (x2)
print('Converting feet to yards: ')
x3=(x/3)
print(x3)