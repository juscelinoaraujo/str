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
    time_t tempo_envio[50], tempo_recebimento[50];
    char carta[1200] = " Mais uma vez as forças e os interesses contra o povo coordenaram-se e novamente se desencadeiam sobre mim. Não me acusam, insultam; não me combatem, caluniam, e não me dão o direito de defesa. Precisam sufocar a minha voz e impedir a minha ação, para que eu não continue a defender, como sempre defendi, o povo e principalmente os humildes. Sigo o destino que me é imposto. Depois de decênios de domínio e espoliação dos grupos econômicos e financeiros internacionais, fiz-me chefe de uma revolução e venci. Iniciei o trabalho de libertação e instaurei o regime de liberdade social. Tive de renunciar. Voltei ao governo nos braços do povo. A campanha subterrânea dos grupos internacionais aliou-se à dos grupos nacionais revoltados contra o regime de garantia do trabalho. A lei de lucros extraordinários foi detida no Congresso. Contra a justiça da revisão do salário mínimo se desencadearam os ódios. Quis criar liberdade nacional na potencialização das nossas riquezas através da Petrobrás e, mal começa esta a funcionar, a onda de agitação se avoluma. A Eletrobrás foi obstaculada até o desespero. Não querem que o trabalhador seja livre.";
    char m1024[1024], m512[512], m256[256], m128[128], m64[64];

    //Construcao das mensagens
    for(int i = 0; i < 1024; i++) {
        m1024[i] = carta[i]; //1024 bytes
    }
    m1024[1024] = '\0';
    
    for(int i = 0; i < 512; i++) {
        m512[i] = carta[i]; //512 bytes
    }
    m512[512] = '\0';

    for(int i = 0; i < 256; i++) {
        m256[i] = carta[i]; //256 bytes
    }
    m256[256] = '\0';

    for(int i = 0; i < 128; i++) {
        m128[i] = carta[i]; //128 bytes
    }
    m128[128] = '\0';

    for(int i = 0; i < 64; i++) {
        m64[i] = carta[i]; //64 bytes
    }
    m64[64] = '\0';
    
    unsigned short porta = 9734;
    
    sockfd  = socket(AF_INET, SOCK_DGRAM, 0);  // criacao do socket
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = inet_addr("127.0.0.1");
    address.sin_port = htons(porta);
    
    len = sizeof(address);
    len_recv = sizeof(address);
    
    printf("O cliente vai enviar as mensagens para o servidor: \n");

    for(int i = 0; i<50; i++){
        tempo_envio[i] = time( (time_t *) 0);  // apontando o ponteiro para null.
        sendto(sockfd,  m64, sizeof(m64),0,(struct sockaddr *) &address, len);
        recvfrom(sockfd, m64, sizeof(m64),0,(struct sockaddr *) &address,&len_recv);
        tempo_recebimento[i] = time( (time_t *) 0);  // apontando o ponteiro para null.

        printf("String vinda do servidor:\n\n");
        for(int j = 0; j < 64; j++) {
            printf("%c", m64[j]);
        }
    }
    close(sockfd);
    exit(0);
}

