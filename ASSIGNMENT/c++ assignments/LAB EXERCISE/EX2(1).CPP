#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();

	int a=10;
	float b=3.14;
	char c='Z';
	const int CONST_VAL =100;

	cout <<"Integer a="<< a<<endl;
	cout <<"Float  b="<< b<<endl;
	cout <<"Character c="<< c<<endl;
	cout <<"Constant CONST_VAL="<< CONST_VAL<<endl;

	int sum = a+ CONST_VAL;
	cout<< "Sum of a CONST_VAL"<< sum;
	getch();
}