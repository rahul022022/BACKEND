#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();
	int marks;
	cout<<"\nEnter marks: ";
	cin>>marks;

	if(marks >=90)
		cout<<"Grade: A+";
	else if(marks>=80)
		cout<<"Grade: A";
	else if(marks >=70)
		cout<<"Grade: B";
	else if(marks >=60)
		cout<<"Grade: C";
	else if(marks >=50)
		cout<<"Grade: D";
	else
		cout<<"Grade F";
	getch();
}