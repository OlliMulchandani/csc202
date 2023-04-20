#include <iostream>
using namespace std;

void compare(int a, int b){
    if (a > b){
        cout << "a is greater than b" << endl;
    } else if (b > a){
        cout << "a is less than b" << endl;
    } else {
        cout << "a is equal to b" << endl;
    }
}

int main(){
    compare(2, 4);
    compare(3, 1);
    compare(2, 2);
}