#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,a[1000],i,min,count=0,start=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    min = 2000;
    while(start!=n)
    {
        start = 0;
        count = 0;
        min = 2000;
        for(i=0;i<n;i++)
        {
            if(a[i]!=0 && min>a[i])
                min = a[i];
        }
        for(i=0;i<n;i++)
        {
            if(a[i]!=0)
            {
                a[i] -= min;
                count++;
            }
        }
        for(i=0;i<n;i++)
        {
            if(a[i]==0)
                start++;
        }
        printf("%d\n",count);
    }
}