#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i,s,t,a,b,m,n,apple[100000],orange[100000],count1=0,count2=0,sum;
    scanf("%d %d",&s,&t);
    scanf("%d %d",&a,&b);
    scanf("%d %d",&m,&n);
    for(i=0;i<m;i++)
        scanf("%d",&apple[i]);
    for(i=0;i<n;i++)
        scanf("%d",&orange[i]);
    for(i=0;i<m;i++)
    {
        sum = 0;
        sum = a+apple[i];
        if(sum>=s && sum<=t)
            count1++;
    }
    for(i=0;i<n;i++)
    {
        sum = 0;
        sum = b+orange[i];
        if(sum>=s && sum<=t)
            count2++;
    }
    printf("%d\n%d",count1,count2);
    
}