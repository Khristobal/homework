num = int(input('enter a number:  '))

i = 0

while True:
    n = num % 10
    if i < n:
        i = n
    else:
        i = i
        num = num // 10
        if num < 1:
            break
print(i)
