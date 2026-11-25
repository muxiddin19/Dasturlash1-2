int[,] matritsa = new int[4, 4] {
 { 1, 2, 3, 4 },
 { 5, 6, 7, 8 },
 { 9, 10, 11, 12 },
 { 13, 14, 15, 16 }
};
int diagonalYigindi = 0;
for (int i = 0; i < 4; i++)
{
 diagonalYigindi += matritsa[i, i];
}
Console.WriteLine($"Diagonal yig'indisi: {diagonalYigindi}");
