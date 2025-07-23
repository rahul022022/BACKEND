#include<stdio.h>
#include<conio.h>

void main()
{
	int n1,n2,op;
	clrscr();

	printf("\nEnter N1:");
	scanf("%d",&n1);
	printf("\nEnter N2:");
	scanf("%d",&n2);

	printf("\n N1 : %d",n1);
	printf("\n N2 : %d",n2);

	printf("\nEnter operator:");
	scanf("%d",&op);

	switch(op)
	{
		case 1:
			n1+n2;
			printf("\nAddition : %d",n1+n2);
			break;
		case 2:
			n1-n2;
			printf("\nSubtraction : %d",n1-n2);
			break;
		case 3:
			n1*n2;
			printf("\nMultiplication : %d",n1*n2);
			break;

		case 4:
			n1/n2;
			printf("\nDivition : %d",n1/n2);
			break;

			default:
			printf("\nInvalid operator:");
	}
	getch();
}