
time = int(input('enter time in seconds: '))

hours = time // 3600
minute = time // 60
min = minute - hours * 60

sec = time - hours * 3600 - min * 60

print(f'{hours}:{min}:{sec}')