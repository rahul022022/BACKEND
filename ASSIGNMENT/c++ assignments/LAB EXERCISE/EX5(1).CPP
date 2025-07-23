#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();
	int arr[5], sum=0;
	float avg;

	cout<<"Enter 5 integers:\n";
	for(int i=0;i<5;i++)
	{
		cin>>arr[i];
		sum +=arr[i];
	}

	avg=(float)sum / 5;

	cout<<"sum="<<sum<<endl;
	cout<<"Average="<<avg;
	getch();
}