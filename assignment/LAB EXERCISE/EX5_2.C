#include<stdio.h>
#include<conio.h>

long factorial_r(int n)
{
	if(n == 0||n == 1)
		return 1;
	else
		return n*factorial_r(n-1);
}

long factorial_i(int n)
{
	long fact =1;
	int i;
	for(i=1;i<=n;i++)
	{
		fact *=i;
	}
	return fact;
}
void main()
{
	int num;
	long fact_rec,fact_iter;
	clrscr();

	printf("\nEnter a number to calculate its factorial:");
	scanf("%d",&num);

	fact_rec = factorial_r(num);
	fact_iter = factorial_i(num);

	printf("\nFactorial using recursion =%ld",fact_rec);
	printf("\nFactorial using interation =%ld",fact_iter);

	getch();
}