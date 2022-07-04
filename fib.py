import time

x = 0
y = 1

i = 0
p = input("How many iterations: ")

while i < int(p):
	i = i + 1

	time.sleep(0.1)	
	print(f"{x} iteration {i}")

	z = x + y
	x = y	
	y = z

print("Tada!")

