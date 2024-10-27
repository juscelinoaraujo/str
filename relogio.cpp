#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>
//#include <windows.h>

int main()
{
    time_t timer;
    while (true)
    {    
        system("clear");
        //system("cls");
        time(&timer);
        printf("%s\n", asctime(localtime(&timer)));
        sleep(1);
    }
    return 0;
}
