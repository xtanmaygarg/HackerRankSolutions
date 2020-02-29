#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,a[200000],t[6],i,max;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=1;i<=5;i++)
        t[i]=0;
    for(i=0;i<n;i++)
    {
        if(a[i]==1)
            t[1]++;
        if(a[i]==2)
            t[2]++;
        if(a[i]==3)
            t[3]++;
        if(a[i]==4)
            t[4]++;
        if(a[i]==5)
            t[5]++;
    }
    max = 0;
    for(i=1;i<6;i++)
    {
        if(t[i]>max)
            max = t[i];
    }
    for(i=1;i<6;i++)
    {
        if(max==t[i])
        {
            printf("%d",i);
            break;
        }
    }
}