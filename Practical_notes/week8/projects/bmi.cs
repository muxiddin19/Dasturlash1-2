
Console.Write("Bo'yingizni metrda kiriting (masalan 1.75): ");
double boy = double.Parse(Console.ReadLine());
Console.Write("Vazningizni kg da kiriting: ");
double vazn = double.Parse(Console.ReadLine());
double bmi = Math.Round(vazn / (boy * boy), 1);
Console.WriteLine($"Sizning BMI ko'rsatkichingiz: {bmi}");
if (bmi < 18.5) Console.WriteLine("Toifa: Kam vazn");
else if (bmi <= 24.9) Console.WriteLine("Toifa: Normal");
else Console.WriteLine("Toifa: Ortiqcha vazn");
