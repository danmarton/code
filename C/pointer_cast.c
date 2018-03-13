#include <stdio.h>

int main()
{
   int x = 0x12345;        //Int32
   
   int *i = &x;            //Operator '&' creates Int-pointer from Int
   
   int j = (int)&x;        //Int-pointer stored as Int, casting suppresses warning
   
   short *s = (short *)&x; //Int-pointer converted to Word-pointer with castinc
   
   char *b = (char *)&x;   //Int-pointer converted to Byte-pointer
   
   printf("%x\n", *i);
   
   printf( "%x\n", *(int *)j );     //Int to Int-pointer, casting required!
   
   printf("%x %x \n", s[0], s[1]);  //See also: showbytes.c
   
   printf("%x %x %x %x \n", *b, b[1], b[2], b[3]);
   
   printf("%x\n", i[0]);
   
   printf( "%x\n", ((int *)j)[0] );
}
