#include <stdio.h>
#include <string.h>

int main()
{
    char palabra[15], palabra2[15];
    int diferencia;
    print("ingrese palabra");
    fgets(palabra,15,stdin);
    print("ingrese palabra");
    fgets(palabra2,15,stdin);

    diferencia = 30 - (strlen(palabra) + strlen(palabra2)) ;

    printf("%s",palabra)
    for (i = 0; i < diferencia - 1 ; i++ )
    {
        printf(".")
    }
    printf("%s",palabra2);
    return 0;
}
