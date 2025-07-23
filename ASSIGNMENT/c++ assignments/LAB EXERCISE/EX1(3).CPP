#include<iostream.h>
#include<conio.h>

class Rectangle
{
	float length, width;
	public:
		void input()
		{
			cout<<"Enter length: ";
			cin>>length;
			cout<<"Enter width: ";
			cin>>width;
		}
		float area()
		{
			return length * width;
		}
};

void main()
{
	clrscr();
	Rectangle r;
	r.input();
	cout<<"Area of rectangle(oop): "<<r.area();
	getch();
}