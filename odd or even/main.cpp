/*
programmers name = Jordan Nolin
date = 9/20/2021
csc160801 comp sci
Topic 3 discussion 10
programs function = program takes users input and states if the number is odd or even.
programiz python ex. https://www.programiz.com/python-programming/examples/odd-even
*/

#include <iostream>
using namespace std;

int main()
{
    int number; // declares number as an intager for user input

    cout << "Enter a number:\n"; // takes user input for number
    cin >> number;

    if(number % 2 == 0) // calculates if num odd or even based on % 2 remander
    {
        cout << number << " is even";
    }
    else
    {
        cout << number << " is odd";
    }
    return 0;
}
