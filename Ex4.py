def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número entre 1 e 100: "))

if 1 <= numero <= 100:
    if eh_primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
else:
    print("Número fora do intervalo de 1 a 100.")
