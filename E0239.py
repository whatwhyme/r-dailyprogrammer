'''Solution to /r/dailprogrammer easy challenge 239 - game of threes.
'''

n = int(input())
while n > 1:
    if n % 3 == 0:
        print(n, 0)
        n = int(n / 3)
    elif n % 3 == 1:
        print(n, -1)
        n = int((n - 1) / 3)
    elif n % 3 == 2:
        print(n, 1)
        n = int((n + 1) / 3)
print(1)
        
        
