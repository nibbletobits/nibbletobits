
#include <iostream>
using namespace std;

int main() {
	int numOne;
	int numTwo;
	int sum;

	cout << "enter two numbers to calculate the sum" << endl;
	cout << "pleas enter your first number:\n";
	cin >> numOne;
	cout << "pleas enter your second number:\n";
	cin >> numTwo;
	sum = numOne + numTwo;

	cout << "the sum one the two numbers is:\n" << sum << endl;

	cout << "enter to 'end'";

	system("pause");

	return 0;

}