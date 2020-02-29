#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    char s[15];
    int n,i;
    scanf("%s",&s);
    n = strlen(s);
    if(s[8]=='A' && s[1]!='2' && s[0]!='1')
    {
        for(i=0;i<n-2;i++)
            printf("%c",s[i]);
    }
    else if(s[8]=='A' && s[1]=='2' && s[0]=='1')
    {
        s[0] = '0';
        s[1] = '0';
        for(i=0;i<n-2;i++)
            printf("%c",s[i]);
    }
    else if(s[8]=='P' && s[1]=='2' && s[0]=='1')
    {
       for(i=0;i<n-2;i++)
            printf("%c",s[i]);
        return 0;
    }
    else if(s[8]=='P')
    {
        if(s[0]=='1' || s[1]=='8' || s[1]=='9')
        {
            s[0] = '2';
        }
        else
            s[0] = '1';
        switch(s[1])
        {
            case '1':
                s[1]='3';
                break;
            case '2':
                s[1]='4';
                break;
            case '3':
                s[1]='5';
                break;
            case '4':
                s[1]='6';
                break;
            case '5':
                s[1]='7';
                break;
            case '6':
                s[1]='8';
                break;
            case '7':
                s[1]='9';
                break;
            case '8':
                s[1]='0';
                break;
            case '9':
                s[1]='1';
                break;
            case '0':
                s[1]='2';
                break;
        }
        for(i=0;i<n-2;i++)
            printf("%c",s[i]);
    }
}