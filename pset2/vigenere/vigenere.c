#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("usage: ./vigenere k, where k is a string of alphabetical characters.\n");
        return 1;
    }
    for(int i = 0, n= strlen(argv[1]);i<n;i++)
    {
        if(isalpha(argv[1][i])== false)
        {
            printf("the key must be a string of alphabetical characters only.\n");
            return 1;
        }
    }
    
    string key = argv[1];
    
    printf("plaintext: ");
    string text = get_string();
    
    int j = 0;
    int m = strlen(key);
    
    printf("ciphertext: ");
    
    for (int i = 0, n = strlen(text); i < n ; i++)
        {
            if (isupper (key[j]))
            {
                if (text[i] >= 65 && text[i] <= 90)
                printf("%c", ((text[i]-65+key[j]-65)%26)+65);
                else if (text[i] >= 97 && text[i] <= 122)
                printf("%c", ((text[i]-97+ key[j]-65)%26)+97);
                else printf("%c", text[i]);
            }
            else 
            {
                if (text[i] >= 65 && text[i] <= 90)
                printf("%c", ((text[i]-65+key[j]-97)%26)+65);
                else if (text[i] >= 97 && text[i] <= 122)
                printf("%c", ((text[i]-97+ key[j]-97)%26)+97);
                else printf("%c", text[i]);
            }
            if (isalpha (text[i]))
            j = (j+1)% m; 
        }
    printf("\n");
    
    
    
    return 0;
}