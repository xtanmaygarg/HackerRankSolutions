#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,k,bill[100000],b,i,sum=0,total;
    scanf("%d %d",&n,&k);
    for(i=0;i<n;i++)
        scanf("%d",&bill[i]);
    scanf("%d",&b);
    for(i=0;i<n;i++)
        sum += bill[i];
    sum = sum - bill[k];
    total = sum/2;
    if(total==b)
        printf("Bon Appetit");
    else
        printf("%d",b-total);
}