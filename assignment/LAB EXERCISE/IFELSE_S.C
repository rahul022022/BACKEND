#include<stdio.h>
#include<conio.h>
void main()
{
	int no,month;
	clrscr();
	printf("\nEnter value :");
	scanf("%d",&no);
	if(no%2==0)
	{
		printf("\n Number is even : %d",no);
	}
	else
	{
		printf("\n Number is odd : %d",no);
	}

	printf("\nEnter month number(1-12):");
	scanf("%d",&month);
	switch(month)
	{
		case 1:
			printf("\n jan");
			break;

		case 2:
			printf("\n feb");
			break;

		case 3:
			printf("\n mar");
			break;

		case 4:
			printf("\n apr");
			break;

		case 5:
			printf("\n may");
			break;

		case 6:
			printf("\n jun");
			break;

		case 7:
			printf("\n jul");
			break;

		case 8:
			printf("\n aug");
			break;

		case 9:
			printf("\n sep");
			break;

		case 10:
			printf("\n oct");
			break;

		case 11:
			printf("\n nov");
			break;

		case 12:
			printf("\n dec");
			break;
		default :printf("\n Invalid ");

	}
	getch();
}