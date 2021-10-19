# include <iostream>
using namespace std;
/*
a = 94-100
a- = 90-93
b = 84 - 89
b- = 77 - 83
c = 74 - 76
c- = 70 -73
d+ = 67 - 69
d = 60 - 66
f = 0 - 59
*/
/*
programmers name = jordan nolin
date = 9/20/2021
csc160801 comp sci
programs function = tests programmers knowledge of && and ||

*/
int main()
{
 int grade;

 string keepGoingAnswer, Y, N;

        cout << "pleas enter your number grade:" << endl;
        cin >> grade;

        // tests input


    while (grade <= 100 && grade >= 1)
    {

             if (grade >= 94)
             {
                 cout << "your grade is an A\n";
             }
             else if (grade >= 90 && grade <= 93)
             {
                 cout << "your grade is an A-\n";
             }
             else if (grade >= 84 && grade <= 89)
            {
                cout << "your grade is an B\n";
            }
            else if (grade >= 77  && grade <= 83)
            {
                cout << "your grade is B-\n";
            }
             else if (grade >= 74 && grade <= 83)
             {
                 cout << "Your grade is an C\n";
             }
             else if (grade >= 70 && grade <= 73)
            {
                cout << "Your grade is an C-\n";
            }
            else if (grade >= 67  && grade <= 69)
            {
                cout << "Your grade is an D+\n";
            }
            else if (grade >= 60 && grade <= 66)
            {
                cout << "Your grade is an D\n";
            }
            else if (grade >= 0 && grade <= 59)
            {
                cout << "Your grade is an F\n";
            }
            else
                throw runtime_error("pleas only enter a number one through one hundred");
    }
	return 0;

    }
