using System;

public delegate void Sajt();

class Program
{
    static Sajt sajt;
    
    static void Main()
    {
            
        for (int i=1; i<6; i++) sajt += delegate {Console.WriteLine("Sajt {0}",i);};
    
        sajt();
    }
}

/*
The five anonymous functions are added to the delegate, but they are only called
when the FOR cycle is finished and the value of i is 6.
*/
