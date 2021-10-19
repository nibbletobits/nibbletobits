#include <iostream>
#include <cctype>
using namespace std;
bool isdigit(char);
int main()
{
    char myChar ; // can be diff values types
    cout << "input myChar" << endl;
    cin >> myChar;

    if (isdigit(myChar))
    {
        cout << myChar << " is digit" << endl;
    }
    else
    {
        cout << myChar << " is not digit" << endl;
    }

    return 0;
}



bool isdigit(char c)
{
    return '0' <= c && c <= '9';
}
