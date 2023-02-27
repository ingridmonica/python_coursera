'''
def é_primo(k):

    primo = True    
    div = 2

    while k > div:
    
        if k % div == 0:
            primo = False
        div = div + 1
    
    return primo

def maior_primo(n):
    k = n        
    while k > 1 and é_primo(k)==False:
        k = k - 1
    return k                                '''


def éPrimo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    
    if x%fator == 0:
        return False
    else:
        return True

n = int(input("Digite um número inteiro: "))

while n > 0:
    if éPrimo(n):
        print(n, "é primo!")
    else:
        print(n, "não é primo :-(")
    
    n = int(input("Digite um número inteiro: "))
