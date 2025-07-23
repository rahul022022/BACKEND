#include<stdio.h>
#include<conio.h>

void main()
{
	int arr[100],n,i,sum=0;
	float average;
	clrscr();

	printf("\nEnter number of elements :");
	scanf("%d",&n);

	printf("\nEnter %d number:",n);
	for(i=0;i<n;i++)
	{
		printf("\nElemnts %d:",i+1);
		scanf("%d",&arr[i]);
		sum +=arr[i];
	}

	average =(float)sum/n;

	printf("\nSum of all elements = %d",sum);
	printf("\nAverage of elements= %f",average);
	getch();
}