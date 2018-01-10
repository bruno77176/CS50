#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

void selectionsort(int array[], int size);

int main(void)
{
    int array[9]={5,58,47,1,3,96,158,4,0};
    printf("%lu\n\n",sizeof(array));
    printf("%lu\n\n",sizeof(array[0]));
    
    int size = sizeof(array)/sizeof(array[0]);
    

    for(int i=0; i<size;i++)
    {
        printf("%i\n",array[i]);
    }
    
    printf("\n");
    selectionsort(array, 9);
    
    for(int i=0; i<size;i++)
    {
        printf("%i\n",array[i]);
    }
}

void selectionsort(int array[], int size)
{
    for(int i=0; i<size; i++)
    {
        for(int j=i+1; j<size;j++)
        {
            if(array[i]>array[j])
            {
                int t = array[j];
                array[j]=array[i];
                array[i]= t;
            }
        }
    }
}
    
