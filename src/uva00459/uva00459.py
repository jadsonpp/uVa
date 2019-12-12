# UVa 00459 - Graph Connectivity

# @authors Guilherme Bodart.

def find(lista,a):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if a==lista[i][j]:
                return i
    return 0

def main():
    num = int(input())
    dic = {'A':1,'B':2,'C':3,'D':4,'E':5,
            'F':6,'G':7,'H':8,'I':9,'J':10,
            'K':11,'L':12,'M':13,'N':14,'O':15,
            'P':16,'Q':17,'R':18,'S':19,'T':20,
            'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    for z in range(num):
        if z == 0:
            vazio = input() 
        no = input()
        lista = []
        x=0
        for i in dic:
            lista.append([])
            lista[x].append(i)
            if i==no:
                break
            x = x + 1
        
        a = input()
        while(a!=""):
            x = find(lista,a[0])
            y = find(lista,a[1])
            if x != y:
                lista[x].extend(lista[y])
                del lista[y]
            try:
                a = input()
            except:
                break
        if z<num-1:
            print(len(lista)-1)
            print()
        else:
            print(len(lista)-1)
    return 0



if __name__ == "__main__":
    main()