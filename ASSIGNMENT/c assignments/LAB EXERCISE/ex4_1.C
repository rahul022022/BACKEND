#include<stdio.h>
#include<conio.h>

void main()
{
	int arr[10],i,max,min,temp,j;

	clrscr();

	printf("\nEnter 10 integers:");
	for(i=0;i<10;i++)
	{
		printf("\nEnter %d:",i+1);
		scanf("%d",&arr[i]);
	}

	max = arr[0];
	min = arr[0];

	for(i=1;i<10;i++)
	{
		if(arr[i]>max)
			max=arr[i];
		if(arr[i]<min)
			min=arr[i];
	}
	// print max and min

	printf("\n Mximum value = %d",max);
	printf("\nMinimum value = %d",min);
	// now challenge array

	for(i=0;i<9;i++)
	{
		for(j=0;j<9-i;j++)
		{
			if(arr[j]>arr[j+1])
			{
				temp =arr[j];
				arr[j] = arr[j+1];
				arr[j + 1] = temp;
			}
		}
	}

	// printf sorted array

	printf("\nArray in ascending order:");
	for(i = 0;i<10;i++)
	{
		printf("%d",arr[i]);
	}
	getch();
}