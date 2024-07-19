from time import sleep
for c in range(10, -1, -1):
    print(f'{c}, ',end='')
    sleep(1)
print('\033[1;31mFogo!!!')