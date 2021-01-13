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


# Better version 



import random 

lot_num = []

while len(lot_num) < 6 :
    aux = random.randint(1,42)
    if aux not in lot_num:
      lot_num.append(aux)
    else:
      continue
print(sorted(lot_num))
