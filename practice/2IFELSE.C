#include<stdio.h>
#include<conio.h>
void main()
{
	int a;
	clrscr();
	printf("\nEnter a value :");
	scanf("%d",&a);
	if(a%2==0)
	{
	printf("\nNmber is even : %d");
	}
	else
	{
	printf("\nNumber is odd : %d");
	}
	getch();
}