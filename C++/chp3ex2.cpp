#include <iostream>
using namespace std;

void print_twice(char phil) {
    cout << phil << phil << endl;
}

int main()
{
    print_twice('a');
    print_twice('b');
    print_twice('c');
    print_twice('d');
    print_twice(2);
    print_twice(3.99);
    print_twice("tryme"); //generates compiling errors, does not compile
    return 0;
}