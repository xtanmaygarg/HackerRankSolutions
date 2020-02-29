#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,a[60],i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(a[i]<38)
            printf("%d\n",a[i]);
        else if((a[i]%5)>2)
            printf("%d\n",((a[i]/5)+1)*5);
        else
            printf("%d\n",a[i]);
    }
}