using System;

public delegate int Sajt();

class Program
{
    static Sajt sajt;
    
    static void Main()
    {
        sajt += Fun1;
        Console.WriteLine(sajt());
        sajt += Fun2;
        Console.WriteLine(sajt());
        sajt += Fun3;
        Console.WriteLine(sajt());
    }
    
    static int Fun1() { Console.WriteLine("One!"); return 1; }
    static int Fun2() { Console.WriteLine("Two!"); return 2; }
    static int Fun3() { Console.WriteLine("Three!"); return (int)null; }
}

//Delegate is overloaded with non-void methods. The return value will come from Fun3, but the other functions are also executed.
//The return value is re-written by each function.
