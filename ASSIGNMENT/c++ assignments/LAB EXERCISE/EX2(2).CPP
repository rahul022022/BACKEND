#include <iostream.h>
#include <conio.h>

void main() {
    clrscr();

    int a = 10;
    float b = 3.5;
    float result;

    // Implicit conversion
    result = a + b;
    cout << "Implicit Conversion (int + float): " << result << endl;

    // Explicit conversion
    result = a + (int)b;
    cout << "Explicit Conversion (int + (int)float): " << result;

    getch();
}
