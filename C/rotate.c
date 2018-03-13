#include <stdio.h>

void main()
{    
   unsigned x = 0x12345678;
   int n = 8;
   unsigned s;
   
   s = ( x & (1<<31>>(n-1)) ) >> (32-n);
   
   printf( "%x\n", (x<<n)+s ); //Left
   
   s = ( x & ~(1<<31>>(31-n)) ) << (32-n);
   
   printf( "%x\n", (x>>n)+s ); //Right
}
