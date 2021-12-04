#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
    char string[50] = "Hello World! there is so much more here";
    char* token = strtok(string, " ");
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }
    return 0;
}