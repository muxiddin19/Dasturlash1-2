Random rnd = new Random();
int maxfiy = rnd.Next(1, 101);
int urinishlar = 0;
while (true)
{
 Console.Write("Taxminingiz: ");
 int taxmin = int.Parse(Console.ReadLine());
 urinishlar++;
 if (taxmin == maxfiy)
 {
 Console.WriteLine($"TABRIKLAYMIZ! {urinishlar} ta urinishda topdingiz!");
 break;
 }
 else if (taxmin > maxfiy) Console.WriteLine("Kichikroq o'ylang!");
 else Console.WriteLine("Kattaroq o'ylang!");
}
