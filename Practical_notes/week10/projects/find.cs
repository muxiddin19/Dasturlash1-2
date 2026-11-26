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

        Console.Write("Qaysi ballni qidiramiz? ");
        int qidirilayotganBall;
        while (!int.TryParse(Console.ReadLine(), out qidirilayotganBall))
        {
            Console.Write("Noto'g'ri qiymat, qaytadan kiriting: ");
        }

        bool topildi = false;
        for (int i = 0; i < ballar.Length; i++)
        {
            if (ballar[i] == qidirilayotganBall)
            {
                Console.WriteLine($"Topildi! Indeks: {i}");
                topildi = true;
                break;
            }
        }
        if (!topildi) Console.WriteLine("Bunday ball topilmadi.");
    }
}
