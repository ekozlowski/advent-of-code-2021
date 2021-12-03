#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    FILE *fptr;
    int depth_increase_count = 0;
    fptr = fopen("../input.txt", "rb");
    char line [1000];
    int vals[4];
    int count = 0;
    while(fgets(line, sizeof line, fptr) != NULL) {
        count += 1;
        vals[0] = vals[1];
        vals[1] = vals[2];
        vals[2] = vals[3];
        vals[3] = atoi(line);
        if (count < 4) {
            continue;
        }
        if ((vals[0] + vals[1] + vals[2]) < (vals[1] + vals[2] + vals[3])) {
            depth_increase_count++;
        }
    }
    fclose(fptr);
    printf("There were %d depth increases.", depth_increase_count);
    return 0;
};