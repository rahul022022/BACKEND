#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();
	int a=10,b=5;

	cout<<"Arithmetic Operators:"<<endl;
	cout<<"a + b=" << a+b<<endl;
	cout<<"a - b=" << a-b<<endl;
	cout<<"a * b=" << a*b<<endl;
	cout<<"a / b=" << a/b<<endl;
	cout<<"a % b=" << a%b<<endl <<endl;

	cout<<"Relational Operators:"<<endl;
	cout<<"a==b:"<<(a == b)<<endl;
	cout<<"a!=b:"<<(a != b)<<endl;
	cout<<"a>b:"<<(a > b)<<endl;
	cout<<"a<b:"<<(a < b)<<endl;
	cout<<"a=>b:"<<(a >= b)<<endl;
	cout<<"a<=b:"<<(a <= b)<<endl <<endl;

	cout<<"Logical Operator:"<<endl;
	cout<<"(a>b) && (b>0):" <<((a>b) && (b>0))<< endl;
	cout<<"(a<b) || (b>0):" <<((a<b) || (b>0))<< endl;
	cout<<"!(a == b):" <<(!(a == b))<< endl << endl;

	cout<<"Bitwish Operators:"<<endl;
	cout<<"a&b="<<(a & b)<<endl;
	cout<<"a|b="<<(a | b)<<endl;
	cout<<"a^b="<<(a ^ b)<<endl;
	cout<<"~a="<<(~a)<<endl;
	cout<<"a<< 1="<<(a<<1)<<endl;
	cout<<"a>> 1="<<(a>>1)<<endl;
	getch();
}