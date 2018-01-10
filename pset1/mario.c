#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    
    do
    {
        printf("Height: ");
        height = get_int();
    }
    while(height<0 || height > 23);
    
    int n = 1 ;
    
    if (height != 0)
    {
        do 
        {
            int i = 0 ;
        
            for (i = height - n ; i > 0 ; i--)
            {
                printf(" ");
            }
        
            for (i = 0 ; i < n + 1 ; i++)
            {
                printf("#");
            }
            printf("\n");
            n++;
        }
        while ( n < height + 1 );
    }
}