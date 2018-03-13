using System;

delegate int PointerType(int x, int y); //The type of the delegate defined with the keyword!

class FunctionClass
{
    public static int Addition(int x, int y) //Here's a function.
    {
        return x + y;
    }

    public static int Multiple(int x, int y) //Here's another one.
    {
        return x * y;
    }
}

class MainClass
{   
    static PointerType Pointer; //Here's the delegate itself! He will store the function pointers.
    
    static void Main()
    {   
        Pointer = new PointerType(FunctionClass.Addition); //Instantiation: New function pointer is created.
        
        Console.WriteLine(Pointer(2,3)); //The pointer is called as a function.
        
        Pointer = FunctionClass.Multiple; //The other function's own pointer gets stored.
        
        Console.WriteLine(Pointer(2,3)); //This call is received by the other function.
    }
}
