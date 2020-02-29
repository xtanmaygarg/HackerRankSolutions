#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,t,a[100000],i,j,k,min;
    scanf("%d %d",&n,&t);
    for(k=0;k<n;k++)
        scanf("%d",&a[k]);
    while(t>0)
    {
        scanf("%d %d",&i,&j);
        min = 100000;
        for(k=i;k<=j;k++)
        {
            if(a[k]<min)
                min = a[k];
        }
        printf("%d\n",min);
        t--;
    }
}