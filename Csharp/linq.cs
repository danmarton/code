using System;
using System.Linq;

class Program
{    
    static void Main()
    {
        Lady[] ladies = new Lady[5];
        
        ladies[0] = new Lady() {name="Alice",num=5};
        ladies[1] = new Lady() {name="Bella",num=4};
        ladies[2] = new Lady() {name="Christina",num=3};
        ladies[3] = new Lady() {name="Dorothy",num=2};
        ladies[4] = new Lady() {name="Emma",num=1};
    }
}

public struct Lady
{
    public string name;
    public int num;
}
