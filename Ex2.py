import math
def verificar_triangulo_e_calcular_area(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Os valores formam um triângulo. A área do triângulo é: {area}")
    else:
        print("Os valores fornecidos não formam um triângulo.")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

verificar_triangulo_e_calcular_area(a, b, c)
