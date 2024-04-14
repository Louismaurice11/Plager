using System;
class program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Enter a num: ");

        int num = Convert.ToInt32(Console.ReadLine());

        if (num > 0)
        {
            Console.WriteLine("Number is positive");
        }
        else if (num == 0)
        {
            Console.WriteLine("Number is 0");
        }
        else
        {
            Console.WriteLine("Number is negative");
        }
        Console.ReadLine();
    }
}