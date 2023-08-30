
#include <iostream> // para: cout
#include <time.h>   // para: time()
#include <unistd.h>
#include <stdlib.h>

using std::cout;
using std::cin;

int main ( )
{

  time_t tempo_real1, tempo_real2, tempo_real3;
  int anos, bissextos, dias, nascimento, data_d, data_m, data_a;
  
  //int tempo_juscelino_nasceu = 86400*365*24 + 86400*6 + 156*86400 + 21*3600;
  // 86400*365*23 -> segundos que passaram de 01/01/1970 a 31/12/1993 (sem contar bissextos)
  // 86400*6 -> acréscimo dos bissextos (1972, 1976, 1980, 1984, 1988, 1992)
  // 156*86400 -> segundos de 01/01/1994 até 05/06/1994
  // 21*3600 -> segundos que passaram de 0:00 até 21:00 em 06/06/1994

  tempo_real1 = time( (time_t *) 0);  // apontando o ponteiro para null.
    
  //tempo_real2 = tempo_real1 - tempo_juscelino_nasceu;
  
  cout << "Digite o ano do seu nascimento: ";
  cin >> data_a;
  cout << "Digite o mes do seu nascimento: ";
  cin >> data_m;
  cout << "Digite o dia do seu nascimento: ";
  cin >> data_d;
  anos = data_a - 1970;
  bissextos = (data_a - 1968)/4;
  dias = data_d - 1;
  switch(data_m) {
  	case 2: 
  		dias += 31;
  		break;
  	case 3: 
		dias += 59;
  		break;
  	case 4: 
  		dias += 90;
  		break;
  	case 5: 
		dias += 120;
  		break;
  	case 6: 
  		dias += 151;
  		break;
  	case 7: 
		dias += 181;
  		break;
  	case 8: 
  		dias += 212;
  		break;
  	case 9: 
		dias += 243;
  		break;
  	case 10: 
  		dias += 273;
  		break;
  	case 11: 
		dias += 304;
  		break;
  	case 12: 
  		dias += 334;
  		break;
  	default: 
  		break;
  }
  if ((data_a % 4) == 0 && data_m > 1) dias++;
  nascimento = 86400*(365*anos + bissextos + dias);
  //tempo_real2 = tempo_real1 - tempo_juscelino_nasceu;
  //cout << "Faz " << tempo_real2 << " segundos desde que Juscelino nasceu." << '\n';
  tempo_real3 = tempo_real1 - nascimento - 10800;
  cout << "Faz " << tempo_real3 << " segundos desde " << data_d << "/" << data_m << "/" << data_a << ".\n";
  //cout << "Faz " << tempo_real1 << " segundos desde 1/1/1970\n";
  //cout << "anos: " << anos << "\n";
  //cout << "bissextos: " << bissextos << "\n";
  //cout << "dias: " << dias << "\n";
     
  exit(0);
}

