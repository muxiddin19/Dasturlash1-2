using System;

class Program
{
    static void Main()
    {
        // 1. Massivni kiritish
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

        // 2. Ballni qidirish
        Console.Write("\nQaysi ballni qidiramiz? ");
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

        // 3. Eng past ballni topib, 0 ga almashtirish
        int minIndeks = 0;
        for (int i = 1; i < ballar.Length; i++)
        {
            if (ballar[i] < ballar[minIndeks])
            {
                minIndeks = i;
            }
        }
        Console.WriteLine($"\nEng past ball: {ballar[minIndeks]} (indeks: {minIndeks})");
        ballar[minIndeks] = 0;

        // 4. Yangilangan massivni chiqarish
        Console.WriteLine("\nYangilangan massiv:");
        foreach (int b in ballar)
        {
            Console.WriteLine(b);
        }
    }
}
