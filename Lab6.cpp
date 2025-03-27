#include <iostream>

using namespace std;

double harmonic(int n) {
    if (n == 1) 
        return 1.0;
    return (1.0 / n) + harmonic(n - 1);
}

double harmonic() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    return harmonic(n);
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << "Harmonic number H_" << n << " = " << harmonic(n) << endl;
    
    cout << "Harmonic number using overloaded function: " << harmonic() << endl;

    return 0;
}
