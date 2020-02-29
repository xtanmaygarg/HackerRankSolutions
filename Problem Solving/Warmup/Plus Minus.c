#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i,n,a[120];
    float pos=0,neg=0,zero=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(a[i]>0)
            pos++;
        else if(a[i]<0)
            neg++;
        else
            zero++;
    }
    printf("%1.6f\n%1.6f\n%1.6f",pos/n,neg/n,zero/n);
}