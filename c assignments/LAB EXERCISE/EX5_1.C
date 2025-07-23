#include<stdio.h>
#include<conio.h>

int fibo_r(int n)
{
	if(n == 0)
		return 0;
	else if(n == 1)
		return 1;

	else
		return fibo_r(n - 1) + fibo_r(n - 2 );
}

int fibo_i(int n)
{
	int a=0,b=1,c,i;
	if(n == 0)
		return a;
	for(i=2;i<=n;i++)
	{
		c= a+b;
		a=b;
		b=c;
	}
	return b;
}
void main()
{
	int n,i;
	int nth_fib_r,nth_fib_i;
	clrscr();

	printf("\n Enter the number of ternms:");
	scanf("%d",&n);

	printf("\n Fibonacci sequence using Recursion:");
	for(i=0;i<n;i++)
	{
		printf("%d",fibo_r(i));
	}

	nth_fib_r=fibo_r(n-1);
	nth_fib_i=fibo_i(n-2);

	printf("\n\n nth fibonacci using recursive: %d",nth_fib_r);
	printf("\n nth fibonacci number using interation: %d",nth_fib_i);
	getch();
}