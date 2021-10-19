#include <iostream>
#include <cctype>
using namespace std;

/*
programmers name = Jordan P. Nolin
date = 10/05/2021
Sum of two numbers  with input validation
programs function = program takes users numbers and prints the sum.
*/

int main() // main takes users input and prints the sum of two numbers to the screen
{
    int num1; // Assigns num1 as type int
    int num2; // Assigns num2 as type int
    int strikes; // assigns strikes to type int and sets variable for while statement
    char keepGoing = 'Y'; // variable for user to break out of loop that adds numbers
    while (keepGoing == 'Y')
    {
        cout << "pleas enter two positive integers that are all digits\n press any key to start:" << endl; // prompts user to input data

        strikes = 0;
        while (strikes <= 2) // creates loop to test the number of times invalid input was entered
        {
            cin.ignore();
            bool areNumbers;
            cout << "enter your first number:" << endl;
            cin >> num1;
            areNumbers = ! cin.fail();
            cout << "enter the second number:" << endl;
            cin >> num2;
            areNumbers = areNumbers && ! cin.fail();
            if (areNumbers) // test if values entered are numbers
            {
                if ((num1 > 0) && (num2 > 0)) // tests that numbers entered are positive
                {
                    int numbersAdded = (num1 + num2); // assigns numbersAdded with sum of num1 and num2
                    cout << "the sum of the numbers entered:\n" << numbersAdded << endl; // prints the sum of numbers if conditions are passed
                    cout << "would you like to keep adding numbers enter 'Y' to keep going?" << endl;
                    cin >> keepGoing;
                    keepGoing = (char) toupper(keepGoing);
                    break;
                }
                else
                {
                    cout << "Only enter positive numbers" << endl;
                    strikes += 1;
                }
            }
            else
            {
                cout << "input must be a digit" << endl;
                strikes +=1;
               cin.ignore();
               cin.clear();
            }
        }
        if (strikes > 2)
        {
            cout << "To many invalid entries" << endl;
            break;
        }
    }

    return 0;
}
