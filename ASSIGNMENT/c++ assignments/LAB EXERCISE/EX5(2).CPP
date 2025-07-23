#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();
	int i,j;
	int a[2][2], b[2][2], sum[2][2];

	cout<<"Enter elements of first 2x2 matrix:\n";
	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
		cin>> a[i][j];

	cout<<"Enter elements of second 2x2 matrix:\n";
	for (i=0;i<2;i++)
		for (j=0;j<2;j++)
		cin>> b[i][j];

	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
		sum[i][j] =  a[i][j] + b[i][j];

	cout<<"Sum of matrices:\n";
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		cout<<sum[i][j]<<" ";
	      cout<<endl;
	 }
	 getch();
}