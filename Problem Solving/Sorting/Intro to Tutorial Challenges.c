#include<stdio.h>
#include<stdlib.h>

int main()
{
    int v,n,a[1000],i;
    scanf("%d",&v);
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(a[i]==v)
        {
            printf("%d",i);
        }
    }
}