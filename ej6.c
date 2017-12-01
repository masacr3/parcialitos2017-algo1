#include <stdio.h>

int main()
{
    int minimo;
    int maximo;
    int n;
    int i;

    printf("ingrese minimo: ");
    scanf("%d",&minimo);
    printf("ingrese maximo: ", );
    scanf("%d",&maximo);
    print("ingrese saltos: ");
    scanf("%d",&n);
    printf("\n");

    for (i = minimo ; i <= maximo ; i = i + n)
    {
        print(" %d  %d", i , i*i);

    }
    return 0;
}
