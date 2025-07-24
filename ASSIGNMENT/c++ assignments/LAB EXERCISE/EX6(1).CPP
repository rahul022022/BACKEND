#include <iostream.h>
#include <conio.h>

class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }

    int subtract(int a, int b) {
        return a - b;
    }

    int multiply(int a, int b) {
        return a * b;
    }

    float divide(int a, int b) {
        if (b == 0) return 0;
        return (float)a / b;
    }
};

void main() {
    clrscr();
    Calculator c;
    int a, b, ch;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "1. Add\n2. Subtract\n3. Multiply\n4. Divide\n";
    cout << "Enter your choice: ";
    cin >> ch;

    switch(ch) {
        case 1: 
                cout << "Result = " << c.add(a, b); 
                break;
        case 2: 
                cout << "Result = " << c.subtract(a, b); 
                break;
        case 3: 
                cout << "Result = " << c.multiply(a, b); 
                break;
        case 4: 
                cout << "Result = " << c.divide(a, b); 
                break;
        default: cout << "Invalid choice!";
    }

    getch();
}
