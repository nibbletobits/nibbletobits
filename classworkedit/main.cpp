#include <iostream>
using namespace std;

int main() {
    bool isValid;
    string secretStr;


    int numLetters = 0;
    int totLength = 0;

    isValid = false;

    cin >> secretStr;
    totLength = secretStr.size() ;

    for(int i=0 ; i<totLength ;i++)
    {
        if (isalpha(secretStr[i]) )
        {
            numLetters++;
        }

    }

    if (numLetters > 3 && totLength > 6)
    {
        isValid = true;
    }


    if (isValid) {
        cout << "Valid" << endl;
    }
    else {
        cout << "Invalid" << endl;
    }

    return 0;
}