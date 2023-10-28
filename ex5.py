def inverter_letras_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]

    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase

frase_original = input("Digite uma frase: ")

frase_invertida = inverter_letras_palavras(frase_original)
print("Frase com as letras das palavras invertidas:", frase_invertida)