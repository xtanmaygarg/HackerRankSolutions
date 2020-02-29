#include<stdio.h>
#include<stdlib.h>

int main()
{
    int d1,d2,m1,m2,y1,y2;
    scanf("%d %d %d",&d2,&m2,&y2);
    scanf("%d %d %d",&d1,&m1,&y1);
    if(y2<y1)
    {
        printf("0");
        return 0;
    }
    else if(y1==y2 && m2<m1)
    {
        printf("0");
        return 0;    
    }
    if(y2>y1)
    {
        printf("%d",10000*(y2-y1));
        return 0;        
    }
    else if(m2>m1)
    {
        printf("%d",(m2-m1)*500);
        return 0;
    }
    else if(d2>d1)
    {
        printf("%d",(d2-d1)*15);
        return 0;        
    }
    else
        printf("0");
}