
def palindromo(palabra = ''):
    if palabra == '':
        palabra = (input("Enter a word: "))

    if palabra == '':
        print('There was no input')
        print('Closing program')
        quit()

    count = 0
    for i in range(len(palabra)):
        if palabra[i].lower() == palabra[len(palabra)-i-1].lower():
            count = count + 1
    if count == len(palabra):
        print('the word {0} is palindrome'.format(palabra.upper()))
        return True
    else:
        print('the word {0} is NOT palindrome'.format(palabra.upper()))
        return False

