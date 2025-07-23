#include<stdio.h>
#include<conio.h>

void main()
{
	int num;
	clrscr();
	printf("\nEnter Number :");
	scanf("%d",&num);

	printf("\n N1 : %d",num);
	if(num%2==0)
	{
		printf("\nNumber Is Even");
	}
	else
	{
		printf("\nNumber Is Odd");
	}

	printf("\n");

	// 2 program
	if(num>0)
	{
		printf("\n Number is positive:");
	}
	else if(num<0)
	{
		printf("\n Number is negitive:");
	}
	else
	{
		printf("\n Number is zero:");
	}
	if(num%3==0 && num%5==0)
	{
		printf("\n Number can divide both");
	}
	else
	{
		printf("\n NUmber cant divide this value");
	}
	getch();
}

