from Palindrome import *
from String_generator import *
from datetime import datetime

start = datetime.now()

palindromo('Kayak')
p = random_string(7)
print(p)

#Encontrar una palabra aleatoria palindroma
flag = False
while not flag:
    if palindromo(random_string(4)):
        flag = True
print ('Conseguido')
end = datetime.now()

print ('Ha tardado {0} segundos'.format(end-start))