#include<stdio.h>
#include<conio.h>

void main()
{
	FILE *fptr;
	char *name;
	clrscr();

	fptr = fopen("test.txt","w");
	printf("\nEnter Name :");
	gets(name);

	fprintf(fptr,"%s",name);
	fclose(fptr);
	printf("\nFile written Successfully");

	fptr=fopen("test.txt","r");
	printf("\nName is : %s",name);
	fclose(fptr);
	getch();
}