#include<stdio.h>
#include<conio.h>

void main()
{
	int choice,i,j,k;
	int a[3][3],b[3][3],result[3][3];

	clrscr();

	printf("\nMatrix Operations menu:");
	printf("1. 2x2 matrix multiplication ");
	printf("2. 3x3 matrix multiplication ");
	printf("\nEnter your choice (1 or 2):");
	scanf("%d",&choice);

	if(chooice == 1)
	{
		printf("\nEnter element of first 2x2 matrix :");
		for(i=0;i<2;i++)
		{
			for(j=0;j<2;j++)
			{
			printf("a[%d][%d]:",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	printf("\nEnter elements of second 2x2 matrix:");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("b[%d][%d]:",i,j);
			scanf("%d",&b[i[[j]);
		}
	}

	printf("\nResult matrix after addition:");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("%d\t",result[i][j]);
		}
		printf("\n");
	}
	else if(choice == 2)
	{
		printf("\nEnter element of first 3x3 matrix :");
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
			printf("a[%d][%d]:",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	printf("\nEnter elements of second 3x3 matrix:");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("b[%d][%d]:",i,j);
			scanf("%d",&b[i[[j]);
		}
	}

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			result[i][j]=0;
		}
	}

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			for(k=0;k<3;k++)
			{
			result[i][j] += a[i][k]*b[k][j];
			}
		}
	}

	printf("\nResult matrix agter multipliaction :");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",tresult[i][j]);
		}
		printf("\n");
	}
	else
	{
		printf("\nInvalid choice please enetr 1 or 2.\n");
	}
	getch();
}