#include <stdio.h>

struct matriz{
  int P1[4];
  int P2[4];
  int P3[4];
};

int main(){
  int recursosExistentes[] = {4, 2, 3, 1};
  int recursosDisponiveis[4];

  struct matriz C = {
      {0, 0, 1, 0},
      {2, 0, 0, 1},
      {0, 1, 2, 0}
      };

  struct matriz R = {
      {2, 0, 0, 1},
      {1, 0, 1, 0},
      {2, 1, 0, 0}
      };

  int Finalizado[3] = {0, 0, 0};
  int processosFinalizados = 0;

  // Calcula os recursos disponíveis inicialmente
  for (int j = 0; j < 4; j++){
    recursosDisponiveis[j] = recursosExistentes[j] - (C.P1[j] + C.P2[j] + C.P3[j]);
  }

  while (processosFinalizados < 3){
    int encontrouProcesso = 0;

    for (int i = 0; i < 3; i++){
      if (Finalizado[i] == 0){
        int podeExecutar = 1;

        for (int j = 0; j < 4; j++){
          if ((i == 0 && R.P1[j] > recursosDisponiveis[j]) ||
              (i == 1 && R.P2[j] > recursosDisponiveis[j]) ||
              (i == 2 && R.P3[j] > recursosDisponiveis[j])){
            podeExecutar = 0;
            break;
          }
        }

        if (podeExecutar){
          for (int j = 0; j < 4; j++){
            if (i == 0)
              recursosDisponiveis[j] += C.P1[j];
            if (i == 1)
              recursosDisponiveis[j] += C.P2[j];
            if (i == 2)
              recursosDisponiveis[j] += C.P3[j];
          }
          Finalizado[i] = 1;
          processosFinalizados++;
          encontrouProcesso = 1;
        }
      }
    }

    if (encontrouProcesso == 0)
    {
      printf("Deadlock detectado!\n");
      return 1;
    }
  }

  printf("Nenhum deadlock detectado. Estado seguro.\n");
  return 0;
}