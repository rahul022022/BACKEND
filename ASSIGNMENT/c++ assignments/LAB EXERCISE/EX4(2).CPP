#include<iostream.h>
#include<conio.h>

int factorial(int n)
{
	if(n <=1)
		return 1;
	else
		return n *factorial(n -1);
}

void main()
{
	clrscr();
	int num;

	cout<<"Enter a number: ";
	cin>> num;

	cout<<"Factorial of"<< num <<" = " <<factorial(num);
	getch();
}