
Console.Write("Taom narxini kiriting: ");
double narx = double.Parse(Console.ReadLine());
Console.Write("Nechta taom: ");
int miqdor = int.Parse(Console.ReadLine());
double taomlarNarxi = narx * miqdor;
double xizmatHaqi = taomlarNarxi * 0.10;
double jami = taomlarNarxi + xizmatHaqi;
Console.WriteLine($"Taomlar narxi: {Math.Round(taomlarNarxi)} so'm");
Console.WriteLine($"Xizmat haqi (10%): {Math.Round(xizmatHaqi)} so'm");
Console.WriteLine($"JAMI TO'LOV: {Math.Round(jami)} so'm");
