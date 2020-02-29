#include<stdio.h>
#include<stdlib.h>

int main()
{
    long int i,a[5],sum=0,max=0,min=1000000000;
    for(i=0;i<5;i++)
        scanf("%ld",&a[i]);
    for(i=0;i<5;i++)
    {
        if(a[i]<min)
            min = a[i];
        if(a[i]>max)
            max = a[i];
        sum += a[i];
    }
    printf("%ld %ld",sum-max,sum-min);
}