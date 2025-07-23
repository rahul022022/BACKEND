#include<stdio.h>
#include<conio.h>

struct Student
{
	char *name;
	int rno;
	float marks;
};

void main()
{
	struct Student s;
	int i;
	clrscr();

	for(i=0;i<3;i++)
	{
		printf("\nEnter student details : %d",i+1);
		printf("\n%d Name :",i+1);
		scanf("%s",s.name);
		printf("\n%d roll no:",i+1);
		scanf("%d",&s.rno);
		printf("\n%d marks :",i+1);
		scanf("%f",&s.marks);
	}
	printf("\nEnter student details :");
	for(i=0;i<3;i++)
	{
		printf("\n name: %s, rno: %d, marks: %f",s.name,s.rno,s.marks);
	}
	getch();
}