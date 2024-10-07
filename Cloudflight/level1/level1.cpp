#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main() {
    ifstream file("level1_5.in");
    ofstream fileout("level16answer.in");
    string line;

    getline(file, line);

    map<char, int> counts{{'W', 0}, {'D', 0}, {'S', 0}, {'A', 0}};
    while (getline(file, line)) {
        for (char c : line) {
            if (counts.find(c) != counts.end()) {  
                counts[c]++;
            }
        }
        fileout << counts['W'] << " " << counts['D'] << " " << counts['S'] << " " << counts['A'] << '\n';
        counts['W'] = 0;
        counts['D'] = 0;
        counts['S'] = 0;
        counts['A'] = 0;
    }
    

    return 0;
}
