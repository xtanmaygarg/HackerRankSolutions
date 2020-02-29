#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int b,c;
    double a;
    float cost;
    int answer;
    scanf("%lf",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    cost = a + (a*b)/100 + (a*c)/100;
    if((int)cost == (int)(cost+0.5))
    {
        answer = (int)cost;
        printf("%d",answer);   
    }
    else
    {
        answer = (int)cost;
        printf("%d",answer+1);        
    }
}