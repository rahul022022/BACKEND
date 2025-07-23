#include<iostream.h>
#include<conio.h>

int globaLvar=100;

void showscope()
{
	int globaLvar=50;
	cout<<"Inside function,local globalvar ="<<globaLvar<<endl;
}

void main()
{
	clrscr();

	cout<<"Outside function,globalvar="<<globaLvar<<endl;
	showscope();
	cout<<"Back in main,globalvar ="<<globaLvar;
	getch();
}