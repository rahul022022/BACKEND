#include<stdio.h>
#include<conio.h>

void main()
{
	int name,marks;
	clrscr();

	printf("\nEnter Student Name: ");
	scanf("%d",&name);
	printf("\nEnter Student Marks: ");
	scanf("%d",&marks);

	if(marks>90)
	{
		printf("\n Grade A");
	}
	else if(marks>75 && marks<=90)
	{
		printf("\n Grade B");
	}
	else if(marks>50 && marks<=75)
	{
		printf("\n Grade C");
	}
	else
	{
		printf("\n Grade D");
	}
	getch();
}