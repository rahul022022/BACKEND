#include<stdio.h>
#include<conio.h>
void main()
{
	int i;
	clrscr();
	// for loop
	printf("\nUsing for loop:");
	for(i=1; i<=10;i++)
	{
		printf("%d",i);
	}

	// while loop
	printf("\nUsing while loop:");
	i=1;
	while(i <=10)
	{
		printf("%d",i);
		i++;
	}
	// do while loop
	printf("\nUsing do while loop :");
	i=1;
	do
	{
		printf("%d",i);
		i++;
	}while (i <=10);
	getch();
}
