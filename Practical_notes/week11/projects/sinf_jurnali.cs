int[,] baholar = new int[3, 4] {
 { 5, 4, 5, 3 }, // 1-talaba
 { 4, 4, 3, 5 }, // 2-talaba
 { 5, 5, 5, 4 } // 3-talaba
};
for (int i = 0; i < 3; i++)
{
 int yigindi = 0;
 for (int j = 0; j < 4; j++)
 {
 yigindi += baholar[i, j];
 }
 double ortacha = (double)yigindi / 4;
 Console.WriteLine($"{i + 1}-talaba o'rtachasi: {ortacha}");
}
