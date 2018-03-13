using System.IO;
using System;

//This code shows how multiple inheritance is emulated by Java and C#

class Program
{
    static void Main()
    {
        C1 aa = new C1();
        I1 bb = new C1();
        I2 cc = new C1();
        
        Console.WriteLine(aa.M1());
        Console.WriteLine(bb.M1());
        Console.WriteLine(cc.M1());
    }
}

interface I1
{
    int M1(); //Access modifiers not accepted because it's automatically public.
}			//Even the word "public" throws error message!

interface I2
{
    int M1();
}

class C1 : I1, I2
{
    public int M1()
    {
        return 0;
    }
    
    int I1.M1() //Access modifiers not accepted!
    {
        return 1;
    }
    
    int I2.M1()
    {
        return 2;
    }
}