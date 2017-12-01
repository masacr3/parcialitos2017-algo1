#include <stdio.h>
#include <string.h>
#define MAX_CARACTER 30

void imprimir_ptos_entre_palabras(char *, char *);

int main ()
{
    char palabra1[MAX_CARACTER], palabra2[MAX_CARACTER];
    printf("palabra 1: ");
    fgets(palabra1,30,stdin);
    palabra1[strlen(palabra1)-1] = '\0';

    printf("palabra 2: ");
    fgets(palabra2,30,stdin);
    palabra2[strlen(palabra2)-1] = '\0';


    imprimir_ptos_entre_palabras(palabra1,palabra2);
    return 0;
}

void imprimir_ptos_entre_palabras(char *cad, char *cad2)
{
    int i , cant_puntos;

    cant_puntos = 30 - ( strlen(cad) + strlen(cad2) );
    printf("%s",cad);

    for (i = 0; i < cant_puntos; i++)
    {
        printf(".");
    }

    printf("%s",cad2);

}
