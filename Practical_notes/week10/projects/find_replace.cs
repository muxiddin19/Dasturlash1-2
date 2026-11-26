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
