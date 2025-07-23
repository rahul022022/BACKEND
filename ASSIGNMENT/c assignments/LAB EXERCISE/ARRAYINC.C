#include<stdio.h>
#include<conio.h>
void main()
{
	int number[5],l;
	clrscr();
	printf("\n 1d array elements");

	for(l=0;l<5;l++)
	{
		printf("\nEnter %d Element:",l);
		scanf("%d",&number[l]);
	}

	printf("\n 2d aaray ");
	int a[3][3],i,j,sum=0;
	printf("\n 2D Array Element");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\nEnter %d row And %d cloumn :",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	printf("\n2 D array Elements arr");
	printf("\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t%d",a[i][j]);
		}
	}

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			sum+=a[i][j];
		}
	}
	printf("\nSum :%d",sum);
	getch();
}