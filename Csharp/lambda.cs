using System;
using System.Linq;

class Program
{    
    static void Main()
    {
        int[] numbers = { 5, 4, 1, 3, 9, 8, 6, 7, 2, 0 };
        
        int[] greater = numbers.Where(n => n > 5);
        
        int evencount = numbers.Count(n => n%2 ==0)
        
        //and so on...
    }
}
