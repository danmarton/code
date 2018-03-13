#include <stdio.h>

int divby16(int x)
{
   return (x-(x>>31<<4)+(x>>31))>>4;
}

int main()
{
   int x = -17;
   printf("%d\n", divby16(x));
   printf("%d\n", x>>4);
}