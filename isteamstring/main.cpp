using namespace std;
#include <iostream>
# include <sstream>
# include <string>

int main() {
    string userInfo;
    userInfo = "Amy Smith 19";
    istringstream verToCallName(userInfo);
    string first;
    string last;
    int userAge;

    verToCallName >> first >> last >> userAge;

     cout  << first << last << userAge;


    return 0;
}
