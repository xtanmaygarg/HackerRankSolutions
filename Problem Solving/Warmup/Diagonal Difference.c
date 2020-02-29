#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[120][120],n,i,j,sum1=0,sum2=0,result;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(i==j)
                sum1 += a[i][j];
            if(i+j == n+1)
                sum2 += a[i][j];
        }
    }
    if(sum1>sum2)
        result = sum1 - sum2;
    else
        result = sum2 - sum1;
    printf("%d",result);
}