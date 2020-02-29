#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i,n,k,height[100],max=0;
    scanf("%d %d",&n,&k);
    for(i=0;i<n;i++)
        scanf("%d",&height[i]);
    for(i=0;i<n;i++)
    {
        if(height[i]>max)
            max = height[i];
    }
    if(max>k)
        printf("%d",max-k);
    else
        printf("0");
}