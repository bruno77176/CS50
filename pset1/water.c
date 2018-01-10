#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    printf("Minutes: ");
    
    do
    {
        n = get_int();
    }
    while(n<0);
    
    printf("Bottles: %i\n",n*12);
    
}