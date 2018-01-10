#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if(argc!=2)
        return 1;
    else if (atoi(argv[1])<3 || atoi(argv[1])>9)
        return 2;
    else
    {
        int d = atoi(argv[1]);
        int table[d][d];
        int k=0;
        
        for (int i=0;i<d;i++)
        {
            for (int j=0;j<d;j++)
            {
                k++;
                table[i][j]=d*d-k;
            }
        }
        if(d%2==0)
        {
            table[d-1][d-2]= 2;
            table[d-1][d-3]=1;
        }
                    
    
        for (int i=0;i<d;i++)
        {
            for (int j=0;j<d;j++)
            {
                if(table[i][j]==0)
                    printf(" _");
                else
                    printf("%2i  ",table[i][j]);
            }
            printf("\n\n");
        }
        
        
        return 0;
    }
}

