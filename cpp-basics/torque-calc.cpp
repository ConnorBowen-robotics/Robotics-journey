#include <iostream>
#include <vector>
using namespace std;
void update(int *a, int *b)
{
   *b = *a - *b;
   *a += *b;
}

int main (void)
{
   int a = 7;
   int b = 5;

   update(&a, &b);
   cout << a << b;
}