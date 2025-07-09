#include<stdio.h>
#include<conio.h>

// declaration
int factorial(int n);

void main()
{
	int num,result;
	clrscr();
	printf("Enter number :");
	scanf("%d",&num);
	// define
	result=factorial(num);
	printf("Fctorial of %d is: %d",num,result);
	getch();
}
int factorial(int n)
{
	int i,fact=1;         //call
	for(i=1;i<=n;i++)
	{
		fact =fact*i;
	}
	return fact;
}