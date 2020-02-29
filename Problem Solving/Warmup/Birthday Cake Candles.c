#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a[100000],n,i,max = 0,count=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(max<a[i])
            max = a[i];
    }
    for(i=0;i<n;i++)
    {
        if(a[i]==max)
            count++;
    }
    printf("%d",count);
}
