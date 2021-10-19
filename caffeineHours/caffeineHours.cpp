/*
programmers name = jordan nolin
date = 9/14/2021
csc160801 comp sci
programs function = calculates caffeine after # hours
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double caffeineMg;

    cout << "enter how many mg of caffeine:" << endl; // takes user input for caffeine in mg
    cin >> caffeineMg;  // caffeine amount (in mg)
    cout << fixed << showpoint;
    cout << setprecision(2);
    /*
    next cout prints amount of caffeine after three listed hours using a half life avrege.
    */
    cout << "After 6 hours: " << caffeineMg * 0.50 << " mg" <<
        "\nAfter 12 hours: " << caffeineMg * 0.25 << " mg" << "\nAfter 24 hours: " << caffeineMg * .0625 << " mg" << endl;


    return 0;
}
