#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();
	char name[100];
	int age;

	cout <<"Enter your name:";
	cin>>name;

	cout<<"\nEnter your age:";
	cin>>age;
	cout<<"WELCOME "<< name << "! you are " << age << " year old.";
	getch();
}