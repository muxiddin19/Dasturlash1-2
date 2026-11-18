Console.Write("Nechta talaba bor? ");
int soni = int.Parse(Console.ReadLine());
int[] ballar = new int[soni];
for (int i = 0; i < soni; i++)
{
 Console.Write($"{i + 1}-talaba balli: ");
 ballar[i] = int.Parse(Console.ReadLine());
}
int yigindi = 0;
int min = ballar[0], max = ballar[0];
foreach (int b in ballar)
{
 yigindi += b;
 if (b < min) min = b;
 if (b > max) max = b;
}
double ortacha = (double)yigindi / soni;
Console.WriteLine($"Yig'indi: {yigindi}");
Console.WriteLine($"Minimum: {min}");
Console.WriteLine($"Maksimum: {max}");
Console.WriteLine($"O'rtacha: {ortacha}");
