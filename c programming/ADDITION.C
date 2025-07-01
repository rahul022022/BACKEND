#include<stdio.h>
#include<conio.h>
void main()
{
	int a,b,c;
	clrscr();
	printf("\nEnter a value of A :");
	scanf("%d",&a);
	printf("\nEnter a value of B :");
	scanf("%d",&b);

	c=a+b;
	printf("\nAddition : %d",c);

	c=a-b;
	printf("\nSubtraction : %d",c);

	c=a*b;
	printf("\nMultiplication : %d",c);

	c=a/b;
	printf("\nDivition : %d",c);
	getch();

}
