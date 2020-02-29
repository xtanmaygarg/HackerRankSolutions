#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,shared,liked=0,count=0;
    scanf("%d",&n);
    shared = 5;
    while(n>0)
    {
        count = shared/2;
        liked = liked + count;
        shared = count*3;
        n--;
    }
    printf("%d",liked);
}