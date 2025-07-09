#include<stdio.h>
#include<conio.h>
void main()
{
	int a = 22,*ptr;
	clrscr();

	ptr =&a;
	printf("\nOriginal value of a: %d",a);

	*ptr = 44;
	printf("\nModified value after using pointer :%d",a);
	getch();
}