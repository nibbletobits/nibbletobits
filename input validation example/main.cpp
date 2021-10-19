#include <iostream>
#include <string>
using namespace std;
int main()
{
    const int A_SCORE = 90,
             B_SCORE = 80,
             C_SCORE = 70,
             D_SCORE = 60,
             MIN_SCORE = 0,
             MAX_SCORE = 100;
    int testscore;

    cout << "Enter your numeric test score and I will \n";
    cout << "tell you the letter grade you earned";

    cin >> testscore;

    if (testscore >= MIN_SCORE && testscore <= MAX_SCORE)
    {
        if (testscore >= A_SCORE)
        {
            cout << "Your grade is A. \n";
        }
        else if (testscore >= B_SCORE)
        {
            cout << "Your grade is B. \n";
        }
        else if (testscore >= C_SCORE)
        {
            cout << "Your grade is C. \n";
        }
        else if (testscore >= D_SCORE)
        {
            cout << "Your grade is D. \n";
        }
        else
        {
            cout << "Your grade is F. \n";
        }
    }
    else
    {
        cout << "That is an invalid score. Run t
