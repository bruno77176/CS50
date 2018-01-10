import cs50

while True:
    print("Height: ", end="")
    height = cs50.get_int()
    if height >=0 and height <=23:
        break

for i in range(height):
    print(" "*(height-i-1), end="")
    print("#"*(i+2))
    