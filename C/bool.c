#include <stdio.h>

void p(int x)
{
   printf("%d\n", x);
}

void main()
{     
   int x = 0xFF000000;
   
   int msb = 0xFF << ((sizeof(int)-1)<<3);
   
   int odd = 0x55555555;
      
   p(x || 0); //Any bit is 1
      
   p(~x && 1); //Any bit is 0
   
   p(x & 0xFF || 0); //Any in LSB is 1
   
   p(~x & msb && 1); //Any in MSB is 0
   
   p(x & odd || 0);  //Any odd bit is 1
}
