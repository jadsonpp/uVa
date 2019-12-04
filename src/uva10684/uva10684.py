'''
    Jadson pereira
    uva10684 - the jackpot

'''



while True:
    try:
        nNumeros = input()
        if(nNumeros != ''):
            nNumeros = int(nNumeros)
            if(nNumeros == 0):
                break
            values = []
            while(nNumeros != 0):
                txt = input()
                lstNum = txt.split()
                tam = len(lstNum)
                for num in lstNum:
                    values.append(int(num))
                nNumeros -= tam
            acc = 0
            acc1 = 0             #Acumulador 
            for i in range(len(values)):
                acc1 += values[i]
                if(acc1<0):
                    acc1 = 0
                else:
                    if(acc1>acc):
                        acc = acc1
            
            if(acc <=0):
                print("Losing streak.")
            else:
                print("The maximum winning streak is "+str(acc)+".")
            acc = 0
            
    except EOFError:
        break
