#include <stdio.h>

void p(int x)
{
   printf("%.8X\n", x);
}

void main()
{     
   char r = 8;
   char l = 8*sizeof(int) - 8;
         
   int i = 0xFF000000;
   
   int ars = i >> r;
   
   int lrs = (unsigned)i >> r;
   
   int ari2log = ars & ~(-1 << l);
   
   int log2ari = lrs |  (-1 << l);
   
   p(ars);
   p(~(-1 << l));
   p(ari2log);
   
   printf("\n");
   
   p(lrs);
   p(-1 << l);
   p(log2ari);
}
