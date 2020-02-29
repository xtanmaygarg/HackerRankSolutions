#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,a[100],i,count=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n-1;i+=0)
    {
        if(a[i+2]==0)
        {
            count++;
            i = i+2;
        }
        else if(a[i+1]==0)
        {
            count++;
            i = i + 1;
        }
    }
    printf("%d",count);
}