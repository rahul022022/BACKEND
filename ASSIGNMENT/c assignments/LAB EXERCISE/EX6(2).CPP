#include<stdio.h>
#include<conio.h>

void countcharacter(char str[])
{
	int i,vowels=0, consonants=0, digits=0, special=0;

	for(i=0;str[i] !='\0';i++)
	{
		char ch= str[i];

	if((ch >= 'A' && ch <='Z') || (ch >='a' && ch <= 'z'))
	{
		if(ch == 'a' || ch == 'e' || ch == 'o' || ch == 'u' ||
		   ch == 'A' || ch == 'I' || ch == 'O' || ch == 'U')
		   {
			vowels++;
	}else{
		consonants++;
	}
	}else if(ch >= '0' && ch <= '9'){
		  digits++;
	}else if(ch != ' '){
		special++;
	}
	}

	printf("\nVowels:%d",vowels);
	printf("\nConsonants:%d",consonants);
	printf("\nDigits: %d",digits);
	printf("\nSpecial characters: %d",special);
}

void main()
{
	char str[100];
	clrscr();

	printf("Enter string:");
	gets(str);
	countcharacter(str);
	getch();
}
