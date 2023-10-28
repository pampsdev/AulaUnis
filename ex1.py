def converter_idade_para_dias_anos_meses_dias(idade):
    dias = idade * 365
    anos = idade
    meses = idade * 12
    dias_restantes = dias % 365
    meses_restantes = dias_restantes // 30
    dias_finais = dias_restantes % 30

    return dias, anos, meses, dias_finais

idade = int(input("Digite a idade em anos: "))

total_dias, anos_totais, meses_totais, dias_totais = converter_idade_para_dias_anos_meses_dias(idade)

print(f"A idade de {idade} anos é aproximadamente: {total_dias} dias, ou {anos_totais} anos, {meses_totais} meses e {dias_totais} dias.")
