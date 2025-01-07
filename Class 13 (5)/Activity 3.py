#Diamond Pattern
n = int(input('Enter the number of rows : '))
if n % 2 == 0:
    halfdiam = int(n / 2)
else:
    halfdiam = int(n / 2) + 1

space = halfdiam - 1

for i in range(1, halfdiam + 1):
    for j in range(1, space + 1):
        print(end = ' ')
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(end = str(num))
        num = num + 1
    print()
    
space = 1

for i in range(1, halfdiam):  
    for j in range(1, space + 1): 
        print(end = ' ')
    space = space + 1
    num = 1
    for j in range(1, 2 * (halfdiam - i)): 
        print(end = str(num))
        num = num + 1
    print()