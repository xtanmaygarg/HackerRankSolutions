#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,i,sea=0,count=0;
    char s[1000000];
    scanf("%d",&n);
    scanf("%s",s);
    i=0;
    while(i<n)
    {
        if(s[i]=='U')
        {
            sea = sea + 1;
        }
        else
        {
            sea = sea - 1;
            if(sea<0)
            {
                count++;
                while(sea<0)
                {
                    i+=1;
                    if(s[i]=='U')
                        sea+=1;
                    else
                        sea-=1;
                }
            }
        }            
        i++;
    }
    printf("%d",count);
}