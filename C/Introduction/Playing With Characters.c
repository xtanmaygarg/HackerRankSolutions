#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch, val[20], val2[100];
    scanf("%c", &ch);
    scanf("%s",val);
    scanf(" %[^\n]s",val2);
    printf("%c\n", ch);
    printf("%s\n", val);
    printf("%s", val2);
    return 0;
}

