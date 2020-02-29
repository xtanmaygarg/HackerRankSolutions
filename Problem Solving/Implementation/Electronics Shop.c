#include<stdio.h>
#include<stdlib.h>

int main()
{
    int c,n,m,i,j,a[1000],b[1000],sum,max=-1;
    scanf("%d %d %d",&c,&n,&m);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<m;i++)
        scanf("%d",&b[i]);
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            sum = a[i] + b[j];
            if(sum<=c && sum>max)
                max = sum;
        }
    }
    printf("%d",max);
}