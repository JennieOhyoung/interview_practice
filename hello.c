#include <stdio.h>

int main(int argc, char** argv)

// {
//     // int arr[5] = {1,2,3,4,5};
//     // int i;

//     char *letters[]=
//         {
//         "A", "B", "C", "D", "E"
//         };
//     int i = 0;

//     for(i=0;i<5;i++)
//         {
//         printf(letters[i]);
//         }   

//     return 0;
// }

char* string = "ABCDE";
for (int i = 0; i < 5; ++i)
{
    printf("%c\n", string[i]);
    return 0;
}
