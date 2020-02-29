#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i,j,k,n,m,a[10],b[10],flag,count=0;
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<m;i++)
        scanf("%d",&b[i]);
    for(i=a[n-1];i<=b[0];i++)
    {
        flag=1;
        for(j=0;j<n;j++)
        {
            if(i%a[j]!=0)
                flag=0;
        }
        if(flag==1)
        {
            flag = 1;
            for(k=0;k<m;k++)
            {
                if(b[k]%i!=0)
                    flag=0;
            }
        }
        if(flag==1)
            count++;
    }
    printf("%d",count);
}