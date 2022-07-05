import time

x = 0
y = 1

i = 0
p = int(input("How many iterations: "))

while i < p:
        i += 1

        time.sleep(0.1)
        print(f"{x} iteration {i}")

        z = x + y
        x = y
        y = z

print("Tada!")
