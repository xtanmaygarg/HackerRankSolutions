#include<stdio.h>
#include<stdlib.h>

int main()
{
    long long int t,b,w,bc,wc,z;
    scanf("%lld",&t);
    while(t>0)
    {
        scanf("%lld %lld",&b,&w);
        scanf("%lld %lld %lld",&bc,&wc,&z);
        if((z+wc)>=bc && (z+bc)>=wc)
            printf("%lld\n",(b*bc+w*wc));
        else if(bc>wc && (z+wc)<=bc)
            printf("%lld\n",(((z+wc)*b)+(w*wc)));
        else if(wc>bc && (z+bc)<=wc)
            printf("%lld\n",(((z+bc)*w)+(b*bc)));
        t--;
    }
}