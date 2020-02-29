#include<stdio.h>
#include<stdlib.h>

int main()
{
    int t,n,value;
    scanf("%d",&t);
    while(t>0)
    {
        scanf("%d",&n);
        value = check(n);
        printf("%d\n",value);
        t--;
    }
}
int check(int a)
{
    int dig,temp,count=0;
    temp = a;
    while(a>0)
        {
            dig = a%10;
            if(dig!=0)
            {
                if(temp%dig==0)
                count++;    
            }
            a = a/10;
        }
    return count;
}