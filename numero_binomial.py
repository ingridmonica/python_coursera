def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat*n
        n = n - 1
    return fat

def numero_binomial(n,k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k)) 


#RESOLUÇÃO PANDA
'''
def fatorial(k):
    #(int) -> int

    #Recebe um inteiro k e retorna o valor de k!

    #Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    

    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1       # o mesmo que cont = cont + 1
        k_fat *= cont   # o mesmo que k_fat = k_fat * cont

    return k_fat

def combinacao(m, n):
    #(int, int) -> int
    #Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)

    return fatorial(m)/(fatorial(n)*fatorial(m-n))

# testes
print("Combinacao(4,2) =", combinacao(4,2))
print("Combinacao(5,2) =", combinacao(5,2))
print("Combinacao(10,4) =", combinacao(10,4))             '''
