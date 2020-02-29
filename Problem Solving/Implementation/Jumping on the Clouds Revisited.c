#include<stdio.h>
#include<stdlib.h>

int main()
{
    int e=100,n,k,c[25],i;
    scanf("%d %d",&n,&k);
    for(i=0;i<n;i++)
        scanf("%d",&c[i]);
    for(i=0;i<n;i+=k)
    {
        if(c[i]==0)
            e -= 1;
        else
            e -= 3;
    }
    printf("%d",e);
}