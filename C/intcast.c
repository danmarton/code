#include <stdio.h>

int main()
{
   short sx = -12345;
   unsigned x = sx;	//Extension happens before conversion (default)
   
   unsigned short usx = sx;
   unsigned y = usx;	//Conversion forced before extension
   
   printf("%.8x\n", x);
   printf("%.8x\n", y);
}