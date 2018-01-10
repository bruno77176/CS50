#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc !=2)
    {
        printf("Vous devez entrer une clé en argument du programme caesar.\nExemple: ./caesar 3\n");
        return 1;
    }

    int k = atoi(argv[1]);

    printf("plaintext: ");
    string text = get_string();
    
    printf("ciphertext: ");
    for(int i=0, n=strlen(text);i<n;i++)
    {
        if(isalpha(text[i]))
        {
            if(isupper(text[i]))
                printf("%c",((text[i]-65 +k)%26)+65);
            else
                printf("%c",((text[i]-97+k)%26)+97);
        }
        else printf("%c",text[i]);
    }
    printf("\n");
    
    return 0;
}