frase = 'We are having a great time in polisinos. there are very smart students here'
contador = 0
for letra in frase:
    if letra not in ['a', 'e', 'i', 'o', 'u','.',' ','A','E','I','O','U']:
        contador +=1
print(contador)
# (not in, else, if not)
