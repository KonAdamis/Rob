import random

x = y = z = n = 0

print(x,y,z)

while n < 2:

    n += 1
    
    for i in range(40):

        r = random.randint(0,5)

        if r == 0:

            x += 1 

        elif r == 1:

            x -= 1

        elif r == 2:

            y += 1

        elif r == 3:

            y -= 1

        elif r == 4:

            z += 1

        elif r == 5:

            z -= 1

        print(x,y,z)

    x = x

    y = y

    z = z
