#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,a[1000],i,sum;
    scanf("%d", &n);
    for(i=0;i<n;i++)
    {
        scanf("%d", &a[i]);
    }
    sum = 0;
    for (i = 0; i < n; i++) {
      sum += a[i];
    }
    printf("%d",sum);
    return 0;
}

