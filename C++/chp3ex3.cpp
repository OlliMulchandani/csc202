#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    add(3, 4);
    cout << "called function" << endl;
    return 0;
}