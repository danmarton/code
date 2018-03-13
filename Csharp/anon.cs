using System;

public delegate void MyDel(int x);

class Program
{
    public static event MyDel Sajt;
    
    static void Main()
    {
        new Listener(); //Run the static constructor!
        
        Sajt(3);
    }
}

public class Listener
{
    static Listener()
    {
        Program.Sajt += delegate(int x) {Console.WriteLine(x*x);};
    }
}
