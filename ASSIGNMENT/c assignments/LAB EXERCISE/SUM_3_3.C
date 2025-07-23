#include<stdio.h>
#include<conio.h>

void main()
{
	int i,n,sum=0;
	clrscr();

	printf("\nEnter number:");
	scanf("%d",&n);

	for(i=0;i<=n;i++)
	{
		sum=sum+i;
	}
	printf("\n Sum of N is: %d",sum);

	getch();
}