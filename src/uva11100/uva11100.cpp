// UVa 11000 - The Trip, 2007

// @authors Guilherme Bodart.

// UVa 00514 - Rails

// @authors Guilherme Bodart.

#include<cstdio>
#include<stack>
#include<vector>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    int lista[10005];
    
    while(scanf("%d",&n) && n){
        for (int i=0;i<n;i++){
            scanf("%d",&lista[i]);
        }
        sort(lista, lista+n);
        int qtdRepetidasMax = 1;
        int qtdRepetidas = 1;

        for(int i=0;i<n-1;i++){
            if(lista[i]==lista[i+1]){
                qtdRepetidas = qtdRepetidas + 1;
            }
            else{
                if(qtdRepetidas>=qtdRepetidasMax){
                    qtdRepetidasMax = qtdRepetidas;
                }
                qtdRepetidas = 1;
            }
        }

        if(qtdRepetidas>=qtdRepetidasMax){
            qtdRepetidasMax = qtdRepetidas;
        }
        vector< vector<int> > mochilas(qtdRepetidasMax+2,vector<int>((n/qtdRepetidasMax)+2,-1));
        

        int i=0;
        int k=0;
        for (int j=0;j<n;j++){
            mochilas[i][k] = lista[j];
            i = i + 1;
            if(i>=qtdRepetidasMax){
                i=0;
                k=k+1;
            }
        }
        printf("%d\n",qtdRepetidasMax);
        for (int i=0;i<qtdRepetidasMax;i++){
            int j=0;
            while(mochilas[i][j]!=-1){
                if(mochilas[i][j+1]==-1){
                    printf("%d",mochilas[i][j]);
                }
                else{
                    printf("%d ",mochilas[i][j]);
                }
                j = j + 1;
            }
            printf("\n");
        } 
    }
}