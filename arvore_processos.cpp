#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <string.h>
//#include <windows.h>

int main(int argc, char *argv[])
{
    //time_t timer;
    //char command[117] = strcat("pstree -a | grep ", argv[1]);
    char command[117] = "pstree -a | grep ";
    strcat(command, argv[1]);
    while (true)
    {    
        system("clear");
        //system("cls");
        //time(&timer);
        //printf("%s\n", asctime(localtime(&timer)));
        system(command);
        sleep(1);
    }
    return 0;
}
