import random as rd

loteria = [None] *6
for i in range(6):
    not_yet = False
    while not_yet == False:
        new_num = rd.randint(0, 40)

        if new_num not in loteria:
            loteria[i] = new_num
            not_yet = True
print("Tu numero de loteria es el: ", loteria)


