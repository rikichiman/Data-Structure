#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct
{
    char c;
    int found;
    int id;
    char type; // 'o' open  - 'c' close
} schar;

schar BChar[6] = {{.c = '(', .id = 1, .type = 'o'},
                  {.c = '[', .id = 2, .type = 'o'},
                  {.c = '{', .id = 3, .type = 'o'},
                  {.c = ')', .id = 1, .type = 'c'},
                  {.c = ']', .id = 2, .type = 'c'},
                  {.c = '}', .id = 3, .type = 'c'}};

typedef struct stack
{
    int cID;
    struct stack *next;
} charS;

charS *stackB;

int checkType(char c, char type) //type can be open or close
{
    for (int i = 0; i < 6; i++)
    {
        if ((c == BChar[i].c) && (BChar[i].type == type))
        {
            return BChar[i].id; // return the ID
        }
    }
    return 0;
}

int testString(char *inS)
{
    charS *sbElt;
    int inLen = strlen(inS);
    int id, n = 0; //number of read characters
    while (*inS != '\0')
    {
        if ((id = checkType(*inS, 'c')) != 0) // it's a closing char
        {
            if (stackB)
            {
                if (id == stackB->cID)
                    stackB = stackB->next; // consume the character
                else
                {
                    return 0;
                }
            }
            else
                return 0;
        }
        else
        {
            sbElt = (charS *)malloc(sizeof(charS));
            sbElt->cID = checkType(*inS, 'o');
            sbElt->next = stackB; // Push it to the stack
            stackB = sbElt;
        }
        inS++; // next character
    }
    if (stackB)
        return 0;
    return 1;
}
int main(void)
{
    int s;
    if (testString("({([])}){}["))
        printf("True");
    else
        printf("False");
    return 1;
}