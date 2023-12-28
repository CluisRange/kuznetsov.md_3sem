using System;

public class Coef
{
    public float vvod(string str)
    {
        while (true)
        {
            Console.WriteLine($"Введите {str}");
            string a = Console.ReadLine();
            try
            {
                return float.Parse(a);
            }
            catch
            {
                Console.WriteLine("Введите число");
            }
        }
    }

    public void init()
    {
        this.a = vvod("A");
        this.b = vvod("B");
        this.c = vvod("C");
    }

    public float a { get; set; }
    public float b { get; set; }
    public float c { get; set; }
}

public class Roots : Coef
{
    float x1, x2;
    public void poluchenie_roots()
    {
        float discr = b * b - 4 * a * c;
        if (discr > 0)
        {
            x1 = (-b - (float)Math.Sqrt(discr)) / (2 * a);
            x2 = (-b + (float)Math.Sqrt(discr)) / (2 * a);
            Console.WriteLine(x1 + " " + x2);
        }
        else if (discr == 0)
        {
            x1 = -b / (2 * a);
            Console.WriteLine(x1 + " ");
        }
        else
        {
            Console.WriteLine("No Roots");
        }
    }
    
}

class Program
{
    static void Main(string[] args)
    {
        Roots a = new Roots();
        a.init();
        a.poluchenie_roots();
    }
}