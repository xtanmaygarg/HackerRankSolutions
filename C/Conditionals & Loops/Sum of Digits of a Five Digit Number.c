#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    long int n;
    int digit,sum = 0;
    scanf("%ld", &n);
    while(n>0)
    {
        digit = n%10;
        sum += digit;
        n = n/10;
    }
    printf("%d",sum);
    return 0;
}

