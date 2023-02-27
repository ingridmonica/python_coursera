
qtd = int(input("Digite o tamanho da sequência de número para ser somado: "))

soma = 0
i = 1

while i <= qtd:
    valor = float(input("Digite um valor a ser somado: "))
    soma = soma + valor
    i = i + 1

print("A soma dos valores digitados é: ", soma)
