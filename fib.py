x = 0
y = 1

p = int(input("How many iterations: "))

for i in range(0, p):
        print(f"{x} iteration {i}")

        z = x + y
        x = y
        y = z

print("Tada!")
