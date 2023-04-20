#include <iostream>
#include <math.h>
using namespace std;

void loop_forever(int n) {
    while (true) {
        cout << "n is now " << n << "." << endl;
        n = n + 1;
    }
}

void recurse_forever(int n) {
    cout << "n is now " << n << "." << endl;
    recurse_forever(n + 1);
}

int main(){
    loop_forever(1);
    recurse_forever(1);
    return 0;
}