#include<stdio.h>
#include<stdlib.h>

int main()
{
    int h[150],i,lengtha,value[10],j,max;
    char a[10];
    for(i=97;i<=122;i++)
        scanf("%d",&h[i]);
    scanf("%s",a);
    lengtha = strlen(a);
    for(i=0;i<lengtha;i++)
    {
        for(j=97;j<=122;j++)
        {
            if(((int)a[i])==j)
            {
                value[i] = h[j];
                break;
            }
        }
    }
    max=0;
    for(i=0;i<lengtha;i++)
    {
        if(value[i]>max)
            max = value[i];
    }
    printf("%d",lengtha*max);
}