#include<stdio.h>
#include<conio.h>

void reversestring(char str[])
{
	int i,len =0;
	char temp;

	while(str[len] != '\0')
	{
		len++;
	}

	for(i=0;i<len /2;i++)
	{
		temp =str[i];
		str[i] =str[len -i -1];
		str[len - i -1] =temp;
	}
}

void main()
{
	char str[100];
	clrscr();

	printf("\nEnter string: ");
	gets(str);

	reversestring(str);
	printf("\nreversed string: %s",str);
	getch();
}
