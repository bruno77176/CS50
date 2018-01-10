/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>

#include "helpers.h"

bool binarysearch(int value, int values[], int min, int max);
/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
   
    return binarysearch(value, values, 0, n);
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            if(values[j]>values[i])
            {
                int t= values[j];
                values[j]=values[i];
                values[i]=t;
            }
        }
    }
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
        else if(value>values[middle])
            return binarysearch(value, values,middle+1, max);
        else return true;
    }
}