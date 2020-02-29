#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int i,j,x1,v1,x2,v2;
    long int sum1,sum2;
    scanf("%d %d %d %d",&x1,&v1,&x2,&v2);
    sum1 = x1;
    sum2 = x2;
    if(x2>x1 && v2>v1)
    {
        printf("NO");
    }
    else
    {
        while(sum1<100000000 && sum2<100000000)
        {
            sum1 += v1;
            sum2 += v2;
            if(sum1 == sum2)
            {
                printf("YES");
                break;
            }
        }
        if(sum1!=sum2)
        {
            printf("NO");
        }
    }
}