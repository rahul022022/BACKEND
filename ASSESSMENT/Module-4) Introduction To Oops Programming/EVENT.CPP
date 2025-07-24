#include<iostream.h>
#include<conio.h>

const double costperhour=22.22;
const double costperminute=0.22;
const double costperdinner=20.22;

class Event
{
	char *eventName;
	char *firstName,*lastName;
	int numGuests, numMinutes, numServers;
	double costForOneServer,totalFoodCost,averageCost,totalCost,depositAmount;

	public:
		void getDetails()
		{
			cout<<"\nEnter Event name: ";
			cin>>eventName;

			cout<<"\nEnter first name: ";
			cin>>firstName;

			cout<<"\nEnter last name: ";
			cin>>lastName;

			cout<<"\nEnter duration of event: ";
			cin>>numMinutes;
		}
		void calculate()
		{
			numServers=numGuests/20;
			if(numGuests%20 !=0)
			{
				numServers +=1;
			}

			double hours=numMinutes/60;
			double minutes=numMinutes%60;
			costForOneServer=(hours * costperhour)+(minutes * costperminute);

			totalFoodCost=numGuests * costperdinner;

			averageCost=totalFoodCost / numGuests;

			totalCost=totalFoodCost+(costForOneServer * numServers);

			depositAmount=totalCost * 0.25;
		}
		void display()
		{
			cout<<"\n********Event managment*********";
			cout<<"\nEvent: "<<eventName;
			cout<<"\nOrganizer : "<<firstName<<" "<<lastName;
			cout<<"\nGuests: "<<numGuests;
			cout<<"\nMinutes: "<<numMinutes;
			cout<<"\nServer needed: "<<numServers;
			cout<<"\ncost for one server: "<<costForOneServer;
			cout<<"\nTotal food cost: "<<totalFoodCost;
			cout<<"\nAverage cost per person:"<<averageCost;
			cout<<"\nTotal cost:"<<totalCost<<"rupees";
			cout<<"\nDeposite: "<<depositAmount<<"rupees";
			cout<<"\n***************************************";
		}
};
void main()
{
	Event e;
	clrscr();
	e.getDetails();
	e.calculate();
	e.display();
	getch();
}