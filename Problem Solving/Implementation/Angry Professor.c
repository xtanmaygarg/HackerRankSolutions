#include<stdio.h>
#include<stdlib.h>

int main()
{
    int t,n,k,a[1000],i,count;
    scanf("%d",&t);
    while(t>0)
    {
        count = 0;
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++)
            scanf("%d",&a[i]);
        for(i=0;i<n;i++)
        {
            if(a[i]<1)
                count++;
        }
        if(count>=k)
            printf("NO\n");
        else
            printf("YES\n");
        t--;
    }
}