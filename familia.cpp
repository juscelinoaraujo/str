#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h> // definição dos sinais de interrupções

void passa_tempo(int anos, int *idade)
{
  sleep(anos);
  *idade += anos;
}

void neto1()
{
  int idade = 0;
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(12, &idade);
    printf("Neto1 morre com %d anos.\n", idade);
    exit(0);
  }
}

void neto2()
{
  int idade = 0;
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(18, &idade);
    printf("Neto2 morre com %d anos.\n", idade);
    exit(0);
  }
}

void filho1()
{
  int idade = 0;
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(12, &idade);
    printf("Filho1 tem seu filho (Neto1) com %d anos.\n", idade);
    neto1();
    passa_tempo(18, &idade);
    printf("Filho1 morre com %d anos.\n", idade);
    exit(0);
  }
}

void filho2()
{
  int idade = 0;
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(14, &idade);
    printf("Filho2 tem seu filho (Neto2) com %d anos.\n", idade);
    neto2();
    passa_tempo(16, &idade);
    printf("Filho2 morre com %d anos.\n", idade);
    exit(0);
  }
}

void pai()
{
  int idade = 0;
  printf("Nasce o pai.\n");
  passa_tempo(14, &idade);
  printf("Pai tem o primeiro filho com %d anos.\n", idade);
  filho1();
  passa_tempo(2, &idade);
  printf("Pai tem o segundo filho com %d anos.\n", idade);
  filho2();
  passa_tempo(44, &idade);
  printf("Pai morre com %d anos.\n", idade);
  exit(0);
}

int main()
{
  /* Variaveis */
  pai();
  
  return 0;
}


