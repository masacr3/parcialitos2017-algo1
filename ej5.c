#include <stdio.h>
#include <string.h>

void invertir_cadena(char *cadena);

int main()
{
    char cadena [100];
    int a ;
    printf("ingrese palabra: ")
    fgets(cadena,100,stdin);
    invertir_cadena(cadena);
    printf("cadena invertida: %s", cadena);
    scanf("%d",&a);
    return 0;
}

void invertir_cadena(char *cadena)
{
    int n = strlen(cadena) - 1;
    int i ;

    for (i = 0; i <= n / 2 ; i++)
    {
        aux = cadena[n - i];
        cadena[n - i] = cadena[i];
        cadena[i] = aux;
    }

}
