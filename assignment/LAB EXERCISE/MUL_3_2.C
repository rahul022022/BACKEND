#include<stdio.h>
#include<conio.h>

void main()
{
	int a,n,ans,range,j;
	clrscr();

	printf("\nEnter number to give its multiplication table:");
	scanf("%d",&n);
	printf("\nEnter range if you want printf table till that:");
	scanf("%d",&range);

	if(range==0)
	{
		for(a=1;a<=10;a++)
		{
			ans=n*a;
			printf("\n %d*%d=%d",n,a,ans);
		}
	}
	else
	{
		for(j=1;j<=range;j++)
		{
			ans=n*j;
			printf("\n %d * %d = %d",n,j,ans);
		}
	}
	getch();
}