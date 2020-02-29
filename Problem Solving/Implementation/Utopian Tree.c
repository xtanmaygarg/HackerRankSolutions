#include<stdio.h>
#include<stdlib.h>

int main()
{
    int t,n,i,height;
    scanf("%d",&t);
    while(t>0)
    {
        height = 1;
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            if(i%2==0)
                height += 1;
            else
                height *= 2;
        }
        printf("%d\n",height);
        t--;
    }
}