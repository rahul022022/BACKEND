#include<iostream.h>
#include<conio.h>
#include<string.h>

void reverseString(char str[])
{
	cout<< "\n Reversed string: ";
	for(int i = strlen(str) -1; i >=0;i--)
	cout<< str[i];
}

void concatenate(char str1[])
{
	char str2[100];
	cout<<"\n Enter string to concatenate: ";
	cin.getline(str2,100);
	strcat(str1,str2);
	cout<<"\n After concatenation:"<<str1;
}

void isPalindrome(char str[])
{
	int len = strlen(str), flag =1;
	for(int i = 0;i < len/2;i++)
	if(str[i] != str[len -i -1])
	{
		flag=0;
		break;
	}
	cout<<"\n The string is "<<(flag ? "": "not")<<"a palindrom.";
}

void copyString(char str[])
{
	char dest[100];
	strcpy(dest, str);
	cout<<"\n String copied:"<< dest;
}

void stringLength(char str[])
{
	cout<<"\n Length:"<< strlen(str);
}

void charFrequency(char str[])
{
	char ch;
	cout<<"\n Enter character: ";
	cin>>ch;
	int count=0;
	for(int i=0; str[i];i++)
	if(str[i] == ch)
	count++;
	cout<<"\n Frequency of"<<ch<<":"<<count;
}

void countVowelsConsonants(char str[])
{
	int v=0,c=0;
	for(int i=0; str[i];i++)
	{
		char ch = str[i];
		if((ch >='A' && ch <='Z')) ch+=32;
		if((ch >='a' && ch <='z'))
		{
			if(ch=='a' ||ch=='e'||ch=='i'||ch=='o'||ch=='u')v++;
			else c++;
		}
	}
	cout<<"\n Vowels: "<< v <<", Consonants: "<<c;
}

void countBlanksDigits(char str[])
{
	int b=0,d=0;
	for(int i=0;str[i];i++)
	{
		if(str[i] ==' ')
		b++;
		else if(str[i] >= '0' && str[i] <='9')d++;
	}
	cout<<"\n Blank: "<< b<<", Digits: "<<d;
}

void main()
{
	clrscr();
	char str[100];
	int ch, cont;

     do{
		cout<<"\n\n====String Operations Menu ===="<< endl;
		cout<<"1. Reverse\n2. Concatenate\n3. Palindrome\.\n4. CopyString\n5. Length\n6. Frequency\n7. Vowels/Consonants\n8. Blank/digits\n9.Exit\n";
		cout<<"Enter yout choice:";
		cin>>ch;
		cin.ignore();

		if(ch >= 1 && ch<=8)
		{
			cout<<"Enter the string: ";
			cin.getline(str, 100);
		}
	switch(ch)
	{
		case 1:
			reverseString(str);
			break;
		case 2:
			concatenate(str);
			break;
		case 3:
			isPalindrome(str);
			break;
		case 4:
			copyString(str);
			break;
		case 5:
			stringLength(str);
			break;
		case 6:
			charFrequency(str);
			break;
		case 7:
			countVowelsConsonants(str);
			break;
		case 8:
			countBlanksDigits(str);
			break;
		case 9:
			cout<<"\n Exiting..";
			return;
		default:
			cout<<"\n Invalid choice!";
			break;
	}

	cout<<"\n\n Do ypu want to continue? (press 1 to continue):";
	cin>>cont;
	cin.ignore();
     }while(cont ==1);
     getch();
}