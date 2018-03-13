using System;
using System.Threading;

class Program
{
    static void Main()
    {
        Console.WriteLine("Main thread has the number {0}",
            Thread.CurrentThread.GetHashCode());
            
            Thread newThread = new Thread(ThreadMethod);
            newThread.Name = "New thread";
            newThread.Start();
			newThread.Join();
    }
    
    static void ThreadMethod()
	{
		Console.WriteLine("{0} has the number {1}", 
			Thread.CurrentThread.Name, 
			Thread.CurrentThread.GetHashCode());
	}
}
