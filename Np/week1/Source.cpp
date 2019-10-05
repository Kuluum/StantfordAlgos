#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;

int main()
{
	ifstream myfile("g3.txt");

	if (!myfile.is_open()) {
		return 1;
	}

	string line;
	getline(myfile, line);
	istringstream iss(line);
	vector<string> tokens{ istream_iterator<string>{iss},
					istream_iterator<string>{} };

	int V = atoi(tokens[0].c_str());
	int E = atoi(tokens[1].c_str());

	vector<vector<int>> W(V, vector<int>(V, 999999));
	while (getline(myfile, line)) {
		istringstream iss(line);
		vector<string> tokens{ istream_iterator<string>{iss},
						istream_iterator<string>{} };
		int a = atoi(tokens[0].c_str());
		int b = atoi(tokens[1].c_str());
		int w = atoi(tokens[2].c_str());
		W[a - 1][b - 1] = w;
	}
	myfile.close();


	for (int k = 0; k < V; k++) {
		for (int i = 01; i < V; i++) {
			for (int j = 0; j < V; j++) {
				W[i][j] = min(W[i][j], W[i][k] + W[k][j]);
			}
		}
		cout << k << "\n";
	}

	bool has_nc = false;
	for (int i = 0; i < V; i++) {
		if (W[i][i] < 0) {
			cout << "neg cycle";
			has_nc = true;
			break;
		}
	}

	
	if (!has_nc) {
		int minp = W[0][0];
		for (int i = 01; i < V; i++) {
			for (int j = 0; j < V; j++) {
				minp = min(minp, W[i][j]);
			}
		}
		cout << minp;
	}

}