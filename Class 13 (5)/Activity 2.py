#Floyd Triangle
print('Floyd Triangle')
n = int(input('Enter the number of iterations : '))

print()
num = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, ' ' ,end = '')
        num = num + 1
    print()
print('This is the final pattern')