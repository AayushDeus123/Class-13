#Star pattern
print('Half pyramid pattern using asterik (*)')
n = int(input('Enter the number of rows for your pattern : '))
print()
for i in range (n):
    for j in range (i+1):
        print('* ' ,end = '')
    print()
print('This is the final pattern')