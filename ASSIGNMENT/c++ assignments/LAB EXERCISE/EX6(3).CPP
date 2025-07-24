#include <iostream.h>
#include <conio.h>

class Person {
public:
    char name[20];
    int age;

    void getDetails() {
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter age: ";
        cin >> age;
    }

    void showDetails() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class Student : public Person {
public:
    int marks;
    void getStudent() {
        getDetails();
        cout << "Enter marks: ";
        cin >> marks;
    }

    void showStudent() {
        showDetails();
        cout << "Marks: " << marks << endl;
    }
};

class Teacher : public Person {
public:
    int salary;
    void getTeacher() {
        getDetails();
        cout << "Enter salary: ";
        cin >> salary;
    }

    void showTeacher() {
        showDetails();
        cout << "Salary: " << salary << endl;
    }
};

void main() {
    clrscr();
    Student s;
    Teacher t;

    cout <<"Enter Student Details\n";
    s.getStudent();

    cout <<"Enter Teacher Details\n";
    t.getTeacher();

    cout <<"Student Info\n";
    s.showStudent();

    cout <<"Teacher Info\n";
    t.showTeacher();

    getch();
}
