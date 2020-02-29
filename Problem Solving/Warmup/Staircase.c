#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i,j,k,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        for(j=n-1;j>i;j--)
        {
            printf(" ");
        }
        for(k=i;k>=0;k--)
        {
            printf("#");
        }
        printf("\n");
    }
}