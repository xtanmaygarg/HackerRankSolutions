#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,i,count = 1;
    char s[100000];
    scanf("%s",s);
    n = strlen(s);
    for(i=0;i<n;i++)
    {
        if((int)s[i]<95)
            count++;
    }
    printf("%d",count);
}