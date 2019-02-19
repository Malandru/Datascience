#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int xmin = atoi(argv[1]);
    int xmax = atoi(argv[2]);
    int ymin = atoi(argv[3]);
    int ymax = atoi(argv[4]);
    // printf("%d\t%d\t%d\n", min, max, nonegative);
    float x, y;
    char buffer[127];
    fgets(buffer, sizeof(buffer), stdin);
    printf("%s", buffer);

    while(scanf("%f", &x) == 1)
    {
        scanf("%f", &y);
        if(x >= xmin && x <= xmax && y >= ymin && y <= ymax)
            printf("%f,%f\n", x, y);
    }
    return 0;
}