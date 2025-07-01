#include<stdio.h>
#include<conio.h>
void main()
{
	int a,b,*p,*q;
	clrscr();
	printf("\nEnter a value A:");
	scanf("%d",&a);
	p=&a;
	printf("\na : %d",a);
	printf("\n*p : %d",*p);
	printf("\np : %u",p);
	printf("\nEnter a value B:");
	scanf("%d",&b);
	q=&b;
	printf("\nb : %d",b);
	printf("\n*q : %d",*q);
	printf("\nq : %u",q);
	getch();
}
