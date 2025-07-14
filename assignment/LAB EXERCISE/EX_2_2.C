#include<stdio.h>
#include<conio.h>

void main()
{
	int n1,n2,n3;
	int largest,smallest,choice;
	clrscr();

	printf("\nEnter Number N1 :");
	scanf("%d",&n1);
	printf("\nEnter Number N2 :");
	scanf("%d",&n2);
	printf("\nEnter Number N3 :");
	scanf("%d",&n3);

	printf("\n Choice:");
	printf("\n largest number");
	printf("\n smallest number");
	printf("\nEnter your choice:");
	scanf("%d",&choice);

	switch(choice)
	{
		case 1:
			if(n1>=n2 && n1>=n3)
			largest =n1;

		       else if(n2>=n1 && n2>=n3)
		       largest =n2;

		       else
		       largest =n3;

		printf("\n Largest number is: %d",largest);
		break;

		case 2:
			if(n1<=n2 && n1<=n3)
			smallest =n1;

			else if(n2<=n1 && n2<=n3)
			smallest =n2;

			else
			smallest =n3;
		printf("\n Smallest number is :%d",smallest);
		break;
		default:
			printf("\nInvalid choice");
	}
	getch();
}

