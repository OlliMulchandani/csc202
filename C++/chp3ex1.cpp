#include <iostream>
using namespace std;

int main()
{
    cout << "First Line." << endl;
    new_line();
    cout << "Second Line." << endl;
    return 0;
}

void new_line()
{
    cout << endl;
}