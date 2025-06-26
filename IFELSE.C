#include<stdio.h>
#include<conio.h>
void main()
{
	int a;
	clrscr();
	printf("\nEnter a number : ");
	scanf("%d",&a);
	if(a>0)
	{
	printf("\nEnter number is positive : %d");
	}
	else
	{
	printf("\nEnter number is negitive : %d");
	}
	getch();
}