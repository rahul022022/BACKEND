#include<iostream.h>
#include<conio.h>

int add(int a,int b)
{
	return a+b;
}

int sub(int a,int b)
{
	return a-b;
}

int multi(int a,int b)
{
	return a*b;
}

int div(int a,int b)
{
	return a/b;
}

void main()
{
	clrscr();
	int num1, num2,choice;

	cout<<"Enter two numbers: ";
	cin>> num1>> num2;

	cout<<"1. Add\2.sub\3.multi\4.div\n";
	cout<<"Enter your choice: ";
	cin>> choice;

	switch(choice)
	{

	case 1:
		cout<<"Result ="<<add(num1, num2);
		break;
	case 2:
		cout<<"Result ="<<sub(num1, num2);
		break;
	case 3:
		cout<<"Result ="<<multi(num1, num2);
		break;
	case 4:
		if(num2 !=0)
			cout<<"Result ="<<div(num1, num2);
		else
			cout<<"Cannot divide by zero!";
		break;
		default: cout<<"Invalid choice!";
	}
	getch();
}