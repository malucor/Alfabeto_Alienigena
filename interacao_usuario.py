import os

const_words = []

adicionar_palavra = int(input("Adicionar quantas palavras? \n"))
print(' \n')

for palavra in range(adicionar_palavra):
    palavra = input("Digite a palavra \n")
    const_words.append(palavra)

os.system('cls') or None

print(f'Palavras =', const_words)