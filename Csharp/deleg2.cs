using System;

public delegate void MyDel();

class Program
{
    private static event MyDel handler;
    
    public static void GiveItToMe(MyDel del)
    {
        handler += del;
    }
    
    static void Main()
    {        
        Functions.Initialize();
        
        if (handler != null) handler();
        else Console.WriteLine("There are no functions signed up yet!");
    }
}

class Functions
{
    private static void Fun1() {Console.WriteLine("Here's a function!");}
    private static void Fun2() {Console.WriteLine("Here's another...");}
    
    public static void Initialize()
    {
        Program.GiveItToMe(Fun1);
        Program.GiveItToMe(Fun2);
    }
    
    /*
    //The static constructor will sign up the two functions...
    static Functions()
    {
        Program.GiveItToMe(Fun1);
        Program.GiveItToMe(Fun2);
    }
    //But we don't know when!
    */
}
