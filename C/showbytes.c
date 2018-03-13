#include <stdio.h>

int main()
{
   int x = 0x12345;
   
   short *s = (short *)&x;    //Word-pointer
   
   char *b = (char *)&x;      //Byte-pointer
   
   printf("%x %x \n", s[0], s[1]);  //Little-endian storage!
   
   printf("%x %x %x %x \n", *b, b[1], b[2], b[3]);
}
