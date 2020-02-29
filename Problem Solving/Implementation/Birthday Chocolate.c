#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,s[100],d,m,i,j,count=0,sum;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&s[i]);
    scanf("%d %d",&d,&m);
    for(i=0;i<n;i++)
    {
        sum=0;
        for(j=i;j<i+m;j++)
        {
            sum += s[j];
        }
        if(sum==d)
            count++;
    }
    printf("%d",count);
}