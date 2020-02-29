#include<stdio.h>
#include<stdlib.h>

int main()
{
    int q,x,y,z,val1,val2;
    scanf("%d",&q);
    while(q>0)
    {
        scanf("%d %d %d",&x,&y,&z);
        if(x>z)
            val1 = x-z;
        else
            val1 = z-x;
        if(y>z)
            val2 = y-z;
        else
            val2 = z-y;
        if(val1>val2)
            printf("Cat B\n");
        else if(val1<val2)
            printf("Cat A\n");
        else
            printf("Mouse C\n");
        q--;
    }
}