#include <iostream>
#include <cmath>
using namespace std;

/*
programmers name = Jordan Nolin
date = 10/09/2021
csc160801 comp sci
Rocket height
programs function = program calculates rockets height till rocket hits 0 using h = vi*t -5t^2. vi =  initial velocity
program output = time and rockets height once per second.
 */

int main() { // main calls program FN.

    int t; // t = time
    double rocketHeight; // height variable
    int vi; // vi = initial velocity

    cout << "input value for vi:\n"; // have to comment out for book
    cin >> vi; // takes in value for velocity

    do
    {
        for(t = 0; rocketHeight >= 0; t++ )
        {
            rocketHeight = (vi * t) - (5 * pow(t,2)); // uses the equation given for rocket height to calculate the new height of the rocket after value taken for initial velocity
            if (t >= 0 && rocketHeight >= 0)
            cout << t << " " << rocketHeight << endl;
        }
    }
    while(rocketHeight > 0);


    return 0;
}
