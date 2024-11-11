#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h> // definição dos sinais de interrupções

/*pid_t tem_filho()
{
  return fork();
}*/

void passa_tempo(int anos, int *idade)
{
  sleep(anos);
  *idade += anos;
}

/*void morre(pid_t pid)
{
  kill(pid, SIGKILL);
}*/

void pai(int *idade[5])
{
  printf("Nasce o pai.\n");
  passa_tempo(14, idade);
  printf("Pai tem o primeiro filho com %d anos.\n", *idade);
  filho1(&idade_filho);
  passa_tempo(2, idade);
  printf("Pai tem o segundo filho com %d anos.\n", *idade);
  filho2();
  printf("Pai morre com %d anos.\n", *idade);
  exit(0);
}

void filho1(int *idade)
{
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(12, idade);
    printf("Filho1 tem seu filho (Neto1) com %d anos.\n", *idade);
    neto1(&idade_neto1);
    printf("Filho1 morre com %d anos.\n", *idade);
    exit(0);
  }
}

void filho2(int *idade)
{
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(14, idade);
    printf("Filho2 tem seu filho (Neto2) com %d anos.\n", *idade);
    neto2(&idade_neto2);
    printf("Filho2 morre com %d anos.\n", *idade);
    exit(0);
  }
}

void neto1(int *idade)
{
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(12, idade);
    printf("Neto1 morre com %d anos.\n", *idade);
    exit(0);
  }
}

void neto2(int *idade)
{
  int pid = fork();
  if (pid == 0)
  {
    passa_tempo(12, idade);
    printf("Neto2 morre com %d anos.\n", *idade);
    exit(0);
  }
}

int main()
{
  /* Variaveis */
  //int idade_pai = 0, idade_filho1 = 0, idade_filho2 = 0, idade_neto1 = 0, idade_neto2 = 0;
  //pid_t pai, filho1, filho2, neto1, neto2;
  int *idade[5];
  pid_t pid;
  pai(idade);
  
  /*printf("Nasce o pai.\n");
  pai = getpid();
  
  passa_tempo(14, &idade_pai);

  if (getpid() == pai)
  {
    printf("Pai tem o primeiro filho com %d anos.\n", idade_pai);
    filho1 = tem_filho();
    dif_f1 = idade_pai;
  }
  
  passa_tempo(2, &idade_pai);
  
  if (getpid() == pai)
  {  
    printf("Pai tem o segundo filho com %d anos.\n", idade_pai);
    filho2 = tem_filho();
    dif_f2 = idade_pai;
  }
  
  passa_tempo(10, &idade_pai);
  
  if (getpid() == filho1)
  {  
    printf("Filho 1 tem seu unico filho com %d anos.\n", idade_pai - dif_f1);
    neto1 = tem_filho();
    dif_n1 = idade_pai;
  }
  
  passa_tempo(4, &idade_pai);
  
  if (getpid() == filho2)
  {
    printf("Filho 2 tem seu unico filho com %d anos.\n", idade_pai - dif_f2);
    neto2 = tem_filho();
    dif_n2 = idade_pai;
  }
  
  passa_tempo(8, &idade_pai);
  
  if (getpid() == neto1)
  {
    printf("Neto1 morre com %d anos.\n", idade_pai - dif_n1);
    morre(neto2);
  }
  
  passa_tempo(6, &idade_pai);
  
  if (getpid() == filho1)
  {
    printf("Filho1 morre com %d anos.\n", idade_pai - dif_f1);
    morre(filho1);
  }
  
  passa_tempo(2, &idade_pai);
  
  if (getpid() == filho2)
  {
    printf("Filho2 morre com %d anos.\n", idade_pai - dif_f2);
    morre(filho2);
  }
  
  passa_tempo(2, &idade_pai);
  
  if (getpid() == neto2)
  {
    printf("Neto2 morre com %d anos.\n", idade_pai - dif_n2);
    morre(neto2);
  }
  
  passa_tempo(12, &idade_pai);
  
  if (getpid() == pai)
  {
    printf("Pai morre com %d anos.\n", idade_pai);
    morre(pai);
  }*/
  
  return 0;
}


