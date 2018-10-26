import math

"""
   calc_vowels(texto)
   entradas: 
    Texto - texto de entrada
   saida:
    numero de vogais no texto 
"""
def calc_vowels(texto):
    contador = 0
    for letra in texto: 
        if letra in ['a', 'e', 'i', 'o', 'u', 'U', 'O', 'I', 'E', 'A']:
            contador+=1
    return contador



