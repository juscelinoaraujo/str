//
//  cliente7.cpp
//  str
//
//  Created by Affonso on 16/05/16.
//  Copyright © 2016 Affonso. All rights reserved.
//

// #include "cliente7.hpp"

// programa cliente7.cpp --> ler um vetor de caracter. Protocolo UDP


#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

int main( )
{
    int sockfd;
    int len;
    socklen_t len_recv;
    struct sockaddr_in address;
    int result;
    //char vetor_ch[4] = {'A','B','C','D'};
    char vetor_ch[4] = {'A'};
    clock_t time_0, time_1;
    float diff_time;
    
    
    unsigned short porta = 9734;
    
    sockfd  = socket(AF_INET, SOCK_DGRAM,0);  // criacao do socket
    
    address.sin_family = AF_INET;
    //address.sin_addr.s_addr = inet_addr("127.0.0.1");
    address.sin_addr.s_addr = inet_addr("192.168.0.11");
    address.sin_port = htons(porta);
    
    len = sizeof(address);
    len_recv = sizeof(address);
    
    printf("O cliente vai enviar a mensagem para o servidor \n");
    
    time_0 = clock();
    sendto(sockfd,  vetor_ch,sizeof(vetor_ch),0,(struct sockaddr *) &address, len);
    recvfrom(sockfd, vetor_ch,sizeof(vetor_ch),0,(struct sockaddr *) &address,&len_recv);
    //sleep(1);
    time_1 = clock();
    diff_time = 1000*((float) time_1 - time_0)/CLOCKS_PER_SEC;
    // send(sockfd,  vetor_ch,sizeof(vetor_ch),0);
    // recv(sockfd, vetor_ch,sizeof(vetor_ch),0);
    //write(sockfd,  vetor_ch,sizeof(vetor_ch));
    //read(sockfd, vetor_ch,sizeof(vetor_ch));
    
    printf( "Caracter vindo do servidor = %c %c %c %c\n",vetor_ch[0],vetor_ch[1],vetor_ch[2],vetor_ch[3]);
    printf("Tempo total = %ld - %ld = %f\n", time_1, time_0, diff_time);

    //printf("Tempo total = %ld - %ld = %f", time_1, time_0, CLOCKS_PER_SEC);
    close(sockfd);
    exit(0);
}

