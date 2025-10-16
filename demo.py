import time

timer =int(input("Enter the time in seconds: "))

for second in range(timer, 0, -1):
    seconds = second % 60
    minutes = int(second / 60) % 60
    hours = int(second / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    