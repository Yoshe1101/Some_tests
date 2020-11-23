import random as rd
import string


def random_string(len):
    palabra = ''
    for i in range(len):
        palabra = palabra + rd.choice(string.ascii_letters)
    return palabra
