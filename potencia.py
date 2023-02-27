# escreva aqui a sua solução
def main():
    num = int(input("Digite um número inteiro: "))
    k = 0
    pot = 0
    
    if num >= 0:

        k = int(input("Digite a potência: "))
        pot = num ** k
        
        print("O resultado de {} elevado a {} é: {}".format(num,k,pot))
    else:
        print("Não existe pontenciação")

main()                                         