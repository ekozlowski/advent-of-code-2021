#include <stdio.h>
#include <stdlib.h>

typedef struct data
{
    int last;
    int depth_increase_count;
} data;

int main()
{
    FILE *fptr;
    data d = {0, 0};
    int current = 0;
    fptr = fopen("../input.txt", "rb");
    char line [1000];
    while(fgets(line, sizeof line, fptr) != NULL) {
        current = atoi(line);
        if (d.last == 0) {
            d.last = current;
            continue;
        } else {
            if (current > d.last) {
                d.depth_increase_count++;
            }
        }
        d.last = current;
    }
    fclose(fptr);
    printf("There are %d depth increases.\n", d.depth_increase_count);
    return 0;
}