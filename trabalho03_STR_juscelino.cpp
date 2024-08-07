
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>   // biblioteca pthread

void swap(int *a, int *b){ 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 
void bubbleSort(int *v, int n){ 
    if (n < 1)return; 
 
    for (int i=0; i<n; i++) 
        if (v[i] > v[i+1]) 
            swap(&v[i], &v[i+1]);  
    bubbleSort(v, n-1); 
}

int main()
{
    //Geracao do vetor aleatorio
    srand(2024);
    int vetor[80000];
    for(int i = 0; i<80000; i++)
    {
        vetor[i] = rand() % 100000;
    }
    
    int *n1a = (int*) malloc(80000*sizeof(int));
    memcpy(n1a, vetor, 80000*sizeof(int));
    
    int *n2a = (int*) malloc(40000*sizeof(int));
    memcpy(n2a, vetor, 40000*sizeof(int));
    int *n2b = (int*) malloc(40000*sizeof(int));
    memcpy(n2b, vetor + 40000, 40000*sizeof(int));
    
    int *n4a = (int*) malloc(20000*sizeof(int));
    memcpy(n4a, vetor, 20000*sizeof(int));
    int *n4b = (int*) malloc(20000*sizeof(int));
    memcpy(n4b, vetor + 20000, 20000*sizeof(int));
    int *n4c = (int*) malloc(20000*sizeof(int));
    memcpy(n4c, vetor + 40000, 20000*sizeof(int));
    int *n4d = (int*) malloc(20000*sizeof(int));
    memcpy(n4d, vetor + 60000, 20000*sizeof(int));
    
    int *n8a = (int*) malloc(10000*sizeof(int));
    memcpy(n8a, vetor, 10000*sizeof(int));
    int *n8b = (int*) malloc(10000*sizeof(int));
    memcpy(n8b, vetor + 10000, 10000*sizeof(int));
    int *n8c = (int*) malloc(10000*sizeof(int));
    memcpy(n8c, vetor + 20000, 10000*sizeof(int));
    int *n8d = (int*) malloc(10000*sizeof(int));
    memcpy(n8d, vetor + 30000, 10000*sizeof(int));
    int *n8e = (int*) malloc(10000*sizeof(int));
    memcpy(n8e, vetor + 40000, 10000*sizeof(int));
    int *n8f = (int*) malloc(10000*sizeof(int));
    memcpy(n8f, vetor + 50000, 10000*sizeof(int));
    int *n8g = (int*) malloc(10000*sizeof(int));
    memcpy(n8g, vetor + 60000, 10000*sizeof(int));
    int *n8h = (int*) malloc(10000*sizeof(int));
    memcpy(n8h, vetor + 70000, 10000*sizeof(int));
    
    int *n16a = (int*) malloc(5000*sizeof(int));
    memcpy(n16a, vetor, 5000*sizeof(int));
    int *n16b = (int*) malloc(5000*sizeof(int));
    memcpy(n16b, vetor + 10000, 5000*sizeof(int));
    int *n16c = (int*) malloc(5000*sizeof(int));
    memcpy(n16c, vetor + 20000, 5000*sizeof(int));
    int *n16d = (int*) malloc(5000*sizeof(int));
    memcpy(n16d, vetor + 15000, 5000*sizeof(int));
    int *n16e = (int*) malloc(5000*sizeof(int));
    memcpy(n16e, vetor + 20000, 5000*sizeof(int));
    int *n16f = (int*) malloc(5000*sizeof(int));
    memcpy(n16f, vetor + 25000, 5000*sizeof(int));
    int *n16g = (int*) malloc(5000*sizeof(int));
    memcpy(n16g, vetor + 30000, 5000*sizeof(int));
    int *n16h = (int*) malloc(5000*sizeof(int));
    memcpy(n16h, vetor + 35000, 5000*sizeof(int));
    int *n16i = (int*) malloc(5000*sizeof(int));
    memcpy(n16i, vetor + 40000, 5000*sizeof(int));
    int *n16j = (int*) malloc(5000*sizeof(int));
    memcpy(n16j, vetor + 45000, 5000*sizeof(int));
    int *n16k = (int*) malloc(5000*sizeof(int));
    memcpy(n16k, vetor + 50000, 5000*sizeof(int));
    int *n16l = (int*) malloc(5000*sizeof(int));
    memcpy(n16l, vetor + 55000, 5000*sizeof(int));
    int *n16m = (int*) malloc(5000*sizeof(int));
    memcpy(n16m, vetor + 60000, 5000*sizeof(int));
    int *n16n = (int*) malloc(5000*sizeof(int));
    memcpy(n16n, vetor + 65000, 5000*sizeof(int));
    int *n16o = (int*) malloc(5000*sizeof(int));
    memcpy(n16o, vetor + 70000, 5000*sizeof(int));
    int *n16p = (int*) malloc(5000*sizeof(int));
    memcpy(n16p, vetor + 75000, 5000*sizeof(int));
}



