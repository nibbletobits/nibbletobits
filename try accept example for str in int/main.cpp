/*
Elijah Walker / edited via Jordan P. Nolin
CSC 160-801
09/20/2021
Topic 3 Discussion: 6. Python Program to Find the Factors of a Number
Based off of https://www.programiz.com/python-programming/examples/factor-number
Finds the factors of a positive number
*/

#include <iostream>
#include <string>
#include <exception>
using namespace std;

int main()
{
	int numFindFactors=-1;     // Positive integer to find factors of
	int loopNum;            // Beginning number of the for loop
    string input;

    while(numFindFactors < 1)
    {
        cout << "please enter a positive number" << endl;
        try
        {
            cin >> input;   // Set Integer to find factors of
            numFindFactors = stoi(input); // will throw
            if(numFindFactors < 1)
            {
                cout << "invalid input." << endl;
            }
        }
        catch (exception& e) // e stores exception (type exception)
        {
            cout << "Invalid input, experienced Standard exception: " << e.what() << endl;  // call what member function of exception type
            numFindFactors=-1;
        }

    }

	cout << "The factors of " << numFindFactors << " are: " << endl;

	// Checks to see if each number is a factor, one at a time, outputs if it is.
	for (loopNum = 1; loopNum <= numFindFactors; ++loopNum)
	{
		if (numFindFactors % loopNum == 0)
		{
			cout << loopNum << endl;
		}
	}

	return 0;
}
