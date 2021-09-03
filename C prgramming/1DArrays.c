#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int num, sum = 0;
    scanf("%d", &num)  ;
    
    int *a = (int *)malloc(sizeof(int) * num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &a[i]);
        sum = sum +a[i];
    }
    printf("%d", sum);
    return 0 ;
}
