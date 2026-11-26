using System;

class Program
{
    static void Main()
    {
        Console.Write("Nechta talaba bor? ");
        int soni;
        while (!int.TryParse(Console.ReadLine(), out soni) || soni <= 0)
        {
            Console.Write("Iltimos, 0 dan katta butun son kiriting: ");
        }

        int[] ballar = new int[soni];
        for (int i = 0; i < soni; i++)
        {
            Console.Write($"{i + 1}-talaba balli: ");
            while (!int.TryParse(Console.ReadLine(), out ballar[i]))
            {
                Console.Write("Noto'g'ri qiymat, qaytadan kiriting: ");
            }
        }

        Array.Sort(ballar);     // o'suvchi tartib
        Array.Reverse(ballar);  // kamayuvchi tartib

        Console.WriteLine("\nBallar (kamayish tartibida):");
        foreach (int b in ballar)
        {
            Console.WriteLine(b);
        }
    }
}
