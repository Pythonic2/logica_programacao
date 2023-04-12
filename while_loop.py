# Verifica verdadeiro ou Falso
# vc  a quantidade exata de repetições



# while talcoisa: faça isso


verificador = True

while verificador:
    pergunta = input("Vc deseja saber a soma de dois numeros? ")
    if pergunta == 'sim':
        numero1 = int(input('Digite o primeiro numero: '))
        numero2 = int(input('Digite o segundo numero: '))
        print(f'A soma é: {numero1 + numero2}')
    else:
        verificador = False



