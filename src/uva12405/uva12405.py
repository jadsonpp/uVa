''''
    uva12405 - ScareCrow
    Jadson Pereira
'''

nCases = input()
case = 1
while(True):
    try:    
        n = input()
        n = int(n)      # Numero de ca
        field = input()      
        scarecrow = 0
        i=0 
        while(i<n):
            if(field[i]=='.'):          
                scarecrow+=1
                #Cobre três celulas <left> e <right>
                i+=3
            else:   
                i+=1
        print("Case "+str(case)+': '+str(scarecrow))
        case += 1

    except EOFError:
        break