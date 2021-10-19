# include <iostream>
using namespace std;

int main()
{
	int r;	// value for red
	int g; // value for green
	int b; // value for blue
	int smallNum;

	cin >> r >> g >> b;

	/*
	the if, elif else statments below find smallest number.
	*/
	if ((r < g) && (r < b))
	{
		smallNum = r;
	}
	else if ((g < r) && (g < b))
	{
		smallNum = g;
	}
	else
	{
		smallNum = b;
	}

	/*
	the below statments remove the grey from rgb
	*/

	int rWithOutGrey = r - smallNum;
	int gWithOutGrey = g - smallNum;
	int bWithOutGrey = b - smallNum;


	cout << rWithOutGrey << " " << gWithOutGrey << " " << bWithOutGrey << endl; // statment prints 3 color values.


	return 0;

}
