#include <iostream>
#include <math.h>
using namespace std;

void sequence(int n)
{
   while (n != 1) {
       cout << n << endl;
       if (n%2 == 0) {      // n is even
           n = n / 2;
       } else {             // n is odd
           n = n * 3 + 1;
       }
   }
}

int main(){
    sequence(1);
    sequence(2);
    sequence(3);
    sequence(4);
    return 0;
}