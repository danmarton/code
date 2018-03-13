#include <stdio.h>

void p(int n)
{
   printf("%.8X\n", n);
}

void main()
{
   int x = 0x12345678;
   
   int lsb = 0xFF;
   int lsi = ~lsb;
   int msb = 0xFF << ((sizeof(int)-1)<<3);
   int msi = ~msb;
   
   p(x & lsb); //00000078
   p(x & lsi); //12345600
   
   p(x | lsb); //123456FF
   p(x | lsi); //FFFFFF78
   
   p(x & msb); //12000000 
   p(x & msi); //00345678
   
   p(x | msb); //FF345678
   p(x | msi); //12FFFFFF
   
   p(x ^ msb); //MSB inverted
   p(x ^ msi); //All but MSB inverted
   p(x ^ lsi); //All but LSB inverted
}
