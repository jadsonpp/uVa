# UVa 00108 - Max Sum

# @authors Guilherme Bodart.

def calculaSoma(i,j,lin,col,lista,dicSoma):
    soma = 0
    for k in range(lin,i+1):
        for q in range(col,j+1):
            try:
                soma = soma + lista[k][q]
            except:
                soma = soma
    return soma


def main():
    while True:
        lista = []
        dicSoma = {}          
        soma = -1000
        maxSoma = -1000
        try:
            dim = int(input())
        except EOFError:
            break
        for n in range(dim):
            lista.append(list(map(int, input().split())))
        for i in range(dim):            
            for j in range(dim):
                for lin in range(i+1):
                    for col in range(j+1):                        
                        soma = calculaSoma(i,j,lin,col,lista,dicSoma)
                        if soma>maxSoma:
                            maxSoma = soma
        print(maxSoma)
    return 0



if __name__ == "__main__":
    main()