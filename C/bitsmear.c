#include <stdio.h>

void main()
{    
   unsigned x = 1025;   //Find the leftmost 1 in the number
   
   //Solution: Bit Smearing!!!
   
   x |= x >> 1;   //Each 1 is smeared to the RIGHT so leading 0's stay intact
   x |= x >> 2;   //Each pair of 1's is smeared, duplicated on bits to right
   x |= x >> 4;   //Each quartet of 1's duplicated on bits to the right
   x |= x >> 8;   //Each byte of 1's duplicated on the bits to the right
   x |= x >> 16;  //Each word of 1's... (just in case)
   
   //Now all bits after the first 1 are also 1's
   //Note: the order of these operations can be reversed!
   
   x ^= x >> 1;   //Let's just clear those trailing 1's with a XOR
   
   printf("%d\n",x); //Print decimal value of result
}
