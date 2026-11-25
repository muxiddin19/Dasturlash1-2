string[][] vazifalar = new string[3][];
vazifalar[0] = new string[] { "Matematika", "Dasturlash" };
vazifalar[1] = new string[] { "Fizika" };
vazifalar[2] = new string[] { "Ingliz tili", "Tarix", "Jismoniy tarbiya" };
for (int i = 0; i < vazifalar.Length; i++)
{
 Console.WriteLine($"Kun {i + 1}: {vazifalar[i].Length} ta vazifa");
}
