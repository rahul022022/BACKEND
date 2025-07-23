#include<stdio.h>
#include<conio.h>
void main()
{
	int a,b,c;
	clrscr();
	printf("\nEnter value A :");
	scanf("%d",&a);
	printf("\nEnter value B :");
	scanf("%d",&b);

	c=a+b;
	printf("\n Addition : %d",c);

	c=a-b;
	printf("\n Subtraction : %d",c);

	c=a*b;
	printf("\n Multiplication : %d",c);

	c=a/b;
	printf("\n Divition : %d",c);

	getch();
}
