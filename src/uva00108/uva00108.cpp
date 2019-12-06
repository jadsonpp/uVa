// UVa 00108 - Maximum Sum

// @authors Guilherme Bodart.

#include<cstdio>
#include<stack>
using namespace std;

int main() {
  
    int listaSoma[100][100];
    int soma = 0;
    int maxSoma;
    int dim;
    scanf("%d",&dim);    
    for(int n=0;n<dim;n++){
        for(int m=0;m<dim;m++){
            scanf("%d",&listaSoma[n][m]);
            if(n>0){
                listaSoma[n][m] = listaSoma[n][m] + listaSoma[n-1][m];
            }
            if(m>0){
                listaSoma[n][m] = listaSoma[n][m] + listaSoma[n][m-1];
            }
            if(n>0 && m>0){
                listaSoma[n][m] = listaSoma[n][m] - listaSoma[n-1][m-1];
            }
            
        }
    }
    maxSoma = -1000;
    for(int i=0;i<dim;i++){         
        for(int j=0;j<dim;j++){
            for(int lin=i;lin<dim;lin++){
                for(int col=j;col<dim;col++){
                    soma = listaSoma[lin][col];
                    if(i>0){
                        soma = soma - listaSoma[i-1][col];
                    }
                    if(j>0){
                        soma = soma - listaSoma[lin][j-1];
                    }
                    if(i>0 && j>0){
                        soma = soma + listaSoma[i-1][j-1];
                    }
                    if(soma > maxSoma){
                        maxSoma = soma;
                    }
                }
            }
        }
    }
    printf("%d\n",maxSoma);

}