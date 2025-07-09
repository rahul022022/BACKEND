#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	char *str1,*str2;
	clrscr();

	printf("\nEnter first string :");
	gets(str1);

	printf("\nEnter second string :");
	gets(str2);

	strcat(str1,str2);
	printf("\nConcatenated string: %s",str1);
	printf("\nLength of Concatenated string: %d",strlen(str1));
	getch();
}
