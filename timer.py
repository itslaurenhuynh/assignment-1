import time

x = int(input("Enter an amount of seconds: "))

def timer(x):
    for i in range(x):
        time.sleep(1)
        print(x)
        x -= 1
    time.sleep(1)
    print('Ding!')

timer(x)