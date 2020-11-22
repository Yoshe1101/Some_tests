


#sg.Window(title="'Here we are'", layout=[[]], margins=(100, 50)).read()

#for i in

#esto = [1, 2, 3, 4, 5, 6, 4, 4, 3, 2, 1, 1]
esto = [None] * 4
for i in range(4):
    esto[i] = (input("Enter a number: "))

cont = 0
while cont != len(esto)-1:
    cont = 0
    for i in range(len(esto)-1):
        if esto[i] > esto[i+1]:
            a = esto[i]
            b = esto[i+1]
            esto[i] = b
            esto[i+1] = a
        else:
            cont = cont+1
print(esto)

