#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float change;
    
    do
    {
        printf("O hai! How much change is owed?\n");
        change = get_float();
    } 
    while (change <0);

    change=round(change*100);
    
    int counter = 0;
    
    while (change >= 25)
    {
        counter ++;
        change = change -25;
    }
    
    while (change >= 10)
    {
        counter ++;
        change = change -10;
    }
    
    while (change >= 5)
    {
        counter ++;
        change = change -5;
    }
    
    while (change >= 1)
    {
        counter ++;
        change = change -1;
    }
    
    printf("%i\n",counter); 

}




