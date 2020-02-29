#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,k,i,a[100],j,count=0;
    scanf("%d %d",&n,&k);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if((a[i]+a[j])%k==0)
                count++;
        }
    }
    printf("%d",count);
}