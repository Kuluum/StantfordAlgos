#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>
using namespace std;

int main()
{
	ifstream myfile ("knapsack_big.txt");

	if (!myfile.is_open()) {
		return 1;
	}
	
	string line;
	getline(myfile, line);
	istringstream iss(line);
	vector<string> tokens{ istream_iterator<string>{iss},
					istream_iterator<string>{} };

	int W = atoi(tokens[0].c_str());
	int N = atoi(tokens[1].c_str());

	vector<pair<int, int>> I;
	while (getline(myfile, line)) {
		istringstream iss(line);
		vector<string> tokens{ istream_iterator<string>{iss},
						istream_iterator<string>{} };
		int v = atoi(tokens[0].c_str());
		int w = atoi(tokens[1].c_str());
		I.push_back(make_pair(v, w));
	}
	myfile.close();

	vector<vector<int>> A(2, vector<int>(W+1));

	for (int i = 1; i < N + 1; i++) {
		for (int x = 0; x < W+1; x++) {
			int a1 = A[0][x];
			int vi = I[i - 1].first;
			int wi = I[i - 1].second;
			int a2 = 0;
			if (x >= wi) {
				a2 = A[0][x - wi] + vi;
			}
			A[1][x] = a1 > a2 ? a1 : a2;
		}
		A[0] = A[1];
		A[1] = vector<int>(W + 1);
		cout << i << "\n";
	}
	cout << A[0][W];
	return 0;
}