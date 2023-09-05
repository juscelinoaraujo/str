/*
 *  ordenacao.cpp
 *  
 *
 *  Created by Luiz Affonso Guedes on 06/03/17.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 */

// UFRN-CT-DCA
// Programa: programa para ordenação de um vetor

// Manipulação de tempo em c,c++
// Programa: programa que usa manipuladores de tempo para 
// medir o desempenho de algoritmos de ordenação


#include <cstdlib>   //qsort
#include <time.h>   // clock(), time()
#include <stdio.h>   // printf()
#include <stdlib.h>  // exit()
#include <unistd.h>  // sleep()
#include <math.h>    // sin()

//Vetores usados pelos métodos de ordenação
int *vetorQuickSort;
int *vetorBubbleSort;

//Função usada pelo qsort para comparar dois numeros
int compare_ints( const void* a, const void* b ) {
	int* arg1 = (int*) a;
	int* arg2 = (int*) b;
	if( *arg1 < *arg2 ) return -1;
	else if( *arg1 == *arg2 ) return 0;
	else return 1;
}

//Algoritmos de ordenação bubble sort
void bubbleSort(int *vetor, int tamanho) {
	int aux;
	for (int i = 0; i < tamanho-1; i++) {
		for (int j = 0; j < tamanho-1; j++) {
			if (vetor[j] > vetor[j+1]) {
				aux = vetor[j];
				vetor[j] = vetor[j+1];
				vetor[j+1] = aux;
			}
		}
	}
}


//Observe que os números são gerados aleatoriamente baseados
//em uma semente. Se for passado a mesma semente, os 
//números aleatórios serão os mesmos
void criarVetor(int tamanhoVetor, int semente){
	srand (semente);
	vetorQuickSort = new int[tamanhoVetor];
	vetorBubbleSort = new int[tamanhoVetor];
	for (int i=0;i<tamanhoVetor;i++){
		vetorQuickSort[i] =  rand()%100000;
        vetorBubbleSort[i] = vetorQuickSort[i]; // utilizar os mesmos valores
		//vetorBubbleSort[i] = rand()%100000;
	}
}



int main ()
{
	//Tamanho do vetor
	int base = 10000;
	int num_testes = 10;
	int tam[num_testes];
	for (int i = 0; i<num_testes; i++) tam[i] = (i + 1)*base;
	clock_t clk[3*num_testes];
	
	
	for (int i = 0; i < 10; i++) {
		//Criar vetor com elementos aleatorios[0,100000] 
		criarVetor(tam[i],233);
		//printf("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n", vetorQuickSort[0], vetorQuickSort[1], vetorQuickSort[2], vetorQuickSort[3], vetorQuickSort[4], vetorQuickSort[5], vetorQuickSort[6], vetorQuickSort[7], vetorQuickSort[8], vetorQuickSort[9], vetorQuickSort[10], vetorQuickSort[11], vetorQuickSort[12], vetorQuickSort[13], vetorQuickSort[14]);
		clk[3*i] = clock();
		//printf("%lu\n", clk[3*i]);
		
		//Ordenar utilizando quickSort
		qsort (vetorQuickSort, tam[i], sizeof(int), compare_ints);
		
		clk[3*i + 1] = clock();
		//printf("%lu\n", clk[3*i+1]);
		//printf("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n", vetorQuickSort[0], vetorQuickSort[1], vetorQuickSort[2], vetorQuickSort[3], vetorQuickSort[4], vetorQuickSort[5], vetorQuickSort[6], vetorQuickSort[7], vetorQuickSort[8], vetorQuickSort[9], vetorQuickSort[10], vetorQuickSort[11], vetorQuickSort[12], vetorQuickSort[13], vetorQuickSort[14]);
		
		
		//Ordenar utilizando bubleSort
		bubbleSort(vetorBubbleSort, tam[i]);
		
		clk[3*i + 2] = clock();
		
		printf("Itera��o: %d\n", i+1);
		printf("Tempo do QuickSort: %lu = %lu - %lu\n", clk[3*i + 1] - clk[3*i], clk[3*i + 1], clk[3*i]);
		printf("Tempo do BubbleSort: %lu = %lu - %lu\n", clk[3*i + 2] - clk[3*i + 1], clk[3*i + 2], clk[3*i + 1]);
	}
	
	exit(0);
}


