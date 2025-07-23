#include<iostream.h>
#include<conio.h>
#include<string.h>

void main()
{
	clrscr();
	char str[50];
	int i, len, flag =1;

	cout<<"Enter a string: ";
	cin>> str;

	len = strlen(str);

	for(i=0; i<len / 2;i++)
	{
		if(str[i] != str[len -i - 1])
	       {
		 flag =0;
		 break;
	       }
	}
	if(flag == 1)
		cout<<"Palindrome";
	else
		cout<<"Not palindrome";
	getch();
}