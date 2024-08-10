
#include <stdio.h>

int getnumbers();
int getxnady(int numbers);
int pontos_cocirculares(int numbers, int x[], int y[]);

int main(void)
{
    int numbers = getnumbers();
    while(numbers != 0)
    {
        int x = getxnady(numbers);
        numbers = getnumbers(); 
    }    
    return 0;

}


int getnumbers(){
    int numbers;
    do {
        scanf("%i", &numbers);
    }while(numbers < 0 || numbers > 100);
    return numbers;
}

int getxnady(int numbers){
    int x[numbers]; 
    int y[numbers];
    for(int i = 0; i < numbers; i++){
        do {
            scanf("%i %i", &x[i], &y[i]);
        }while((x[i] <-10000 || x[i] > 10000) || (y[i] <-10000 || y[i] > 10000));   
    }
    return pontos_cocirculares(numbers, x, y);
}

int pontos_cocirculares(int numbers, int x[], int y[])
{

    int coordenadas[numbers];
    int coo[2];
    for (int i =0; i< numbers; i++){
        coo[0] = x[i]; 
        coo[1] = y[i];
        for(int j = 0; i < numbers; i++){
            coordenadas[j] = coo;
        }
        printf("%i", coordenadas[0]);
    }

    return 0;
}
