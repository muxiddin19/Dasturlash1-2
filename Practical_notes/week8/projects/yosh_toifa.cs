
Console.Write("Yoshingizni kiriting: ");
string kiritilgan = Console.ReadLine();
if (int.TryParse(kiritilgan, out int yosh))
{
 if (yosh <= 12) Console.WriteLine("Toifa: Bola");
 else if (yosh <= 17) Console.WriteLine("Toifa: O'smir");
 else if (yosh <= 59) Console.WriteLine("Toifa: Kattalar");
 else Console.WriteLine("Toifa: Keksa");
}
else
{
 Console.WriteLine("Noto'g'ri son kiritildi!");
}
