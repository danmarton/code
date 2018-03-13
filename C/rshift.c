#include <stdio.h>

void p(int x)
{
   printf("%.8X\n", x);
}

void main()
{     
   unsigned u = 0xFF000000;
        int s = (int)u     //Same hex value!
   
   p(u>>4);                //Unsigned shift (logical)
   
   p((int)u>>4);           //Signed shift (arithmetical)
   
   p((unsigned)s>>4);      //Unsigned again
   
}
