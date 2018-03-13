#include <stdio.h>

void p(int x)
{
   printf("%.8X\n", x);
}

void main()
{     
   unsigned x = 24;
   
   x ^= x >> 1;   //First of each bit pair becomes its XOR sum
   x ^= x >> 2;   //First of each bit quartet becomes its XOR sum
   x ^= x >> 4;   //First of each byte becomes...
   x ^= x >> 8;   //First of each word...
   x ^= x >> 16;  //First bit becomes XOR sum of whole integer
   
   printf("%d\n",x&1); //Return 1st bit
}
