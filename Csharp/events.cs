using System;

public delegate void MyDel(int i);

class Program
{   
    static Raiser r;
    
    static void Main()
    {
        r = new Raiser();
        
        r.Raise(3); //Event raised without subscribers
        
        new Listener(r); //This object is created only to run the constructor.
        
        r.Raise(3); //Event raised with subscribers.
    }
}

public class Raiser
{
    private event MyDel Handler; //Here is the event!
    
    public void Giveittome(MyDel d) { Handler += d; } //Here's the proxy method.
    
    public void Raise(int i)
    { 
        if (Handler != null) Handler(i); //See if there are any subscribed functions.
        
        else Console.WriteLine("No subscribers yet!");
    }
}

public class Listener
{
    private void Fun1(int x) { Console.WriteLine("Double = {0}", x+x); }
    private void Fun2(int x) { Console.WriteLine("Square = {0}", x*x); }
    
    public Listener(Raiser r) //We have to reach the raiser object and its proxy method.
    {
        r.Giveittome(Fun1);
        r.Giveittome(Fun2);
    }
}
