#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,i=1,p,count=0;
    scanf("%d",&n);
    scanf("%d",&p);
    if((p-i)>=(n-p))
    {
        if(n%2==0)
        {
            while(n>p)
            {
                count++;
                n-=2;
            }
        }
        else
        {
            while(n>p+1)
            {
                count++;
                n-=2;
            }
        }
    }
    else
    {
        while(i<p)
        {
            count++;
            i+=2;
        }
    }
    printf("%d",count);
        
}