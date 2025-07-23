#include <iostream.h>
#include <conio.h>

class BankAccount {
private:
    int balance;

public:
    BankAccount() {
        balance = 0;
    }

    void deposit(int amount) {
        balance += amount;
        cout << "Deposited: " << amount << endl;
    }

    void withdraw(int amount) {
        if (amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: " << amount << endl;
        } else {
            cout << "Insufficient balance!" << endl;
        }
    }

    void displayBalance() {
        cout << "Current Balance: " << balance << endl;
    }
};

void main() {
    clrscr();
    BankAccount acc;
    int choice, amt;

    do {
        cout << "\n1. Deposit\n2. Withdraw\n3. Show Balance\n4. Exit\nEnter choice: ";
        cin >> choice;

        switch(choice) {
            case 1:
                cout << "Enter amount to deposit: ";
                cin >> amt;
                acc.deposit(amt);
                break;
            case 2:
                cout << "Enter amount to withdraw: ";
                cin >> amt;
                acc.withdraw(amt);
                break;
            case 3:
                acc.displayBalance();
                break;
        }
    } while(choice != 4);

    getch();
}
