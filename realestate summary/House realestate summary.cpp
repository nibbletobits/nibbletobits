/*
programmers name = jordan nolin
date = 8/31/2021
csc160801 comp sci
program takes iser input in the form of intagers, "no double/float values"
program outputs: listing price, change in price, monthly mortgage at curent rate.
*/

#include <iostream>
using namespace std;

int main() {

	int current_price, lastmonths_price, change;

	cout << "pleas enter the current price:\n"; cin >> current_price; cout << "pleas enter last months price:\n"; cin >> lastmonths_price;// asks user to input new/old price and takes input for the current price and last months housing price.
	
	change = (current_price - lastmonths_price);

	cout << "This house is $" << current_price << "."
		<< " The change is $" << change << " since last month." << endl; // line prints out the change from last month
	cout << "The estimated monthly mortgage is $" << (current_price * 0.051) / 12 << "." << endl; // line calculates and prints current mortgage estimated.

	return 0;
}
