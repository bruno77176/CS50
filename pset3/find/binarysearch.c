#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

bool binarysearch(int value, int values[], int min, int max);

int main(void)
{
int value = get_int();
int values[9]={2,5,8,34,59,394,445,555,998};

if(binarysearch(value, values, 0, 9))
    printf("value found in values");
else
    printf("value not found in values");
}

bool binarysearch(int value, int values[], int min, int max)
{
    if(min>max)
        return false;
    else
    {
        int middle = (min+max)/2;
        
        if(value< values[middle])
            return binarysearch(value, values,min, middle-1);
        else if(value<values[middle])
            return binarysearch(value, values,middle+1, max);
        else return true;
    }
}