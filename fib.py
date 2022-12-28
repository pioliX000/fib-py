import time

x = 0
y = 1

p = int(input("How many iterations: "))

for i in range(0, p):
        time.sleep(0.1)
        print(f"{x} iteration {i}")

        z = x + y
        x = y
        y = z

print("Tada!")
