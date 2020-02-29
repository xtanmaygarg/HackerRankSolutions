#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n,a[1000],i,highest,lowest,count1=0,count2=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    highest = a[0];
    lowest = a[0];
    for(i=1;i<n;i++)
    {
        if(a[i]<lowest)
        {
            lowest = a[i];             
            count2++;
        }
        if(a[i]>highest)
        {
            highest = a[i];
            count1++;            
        }
    }
    printf("%d %d",count1,count2);
}