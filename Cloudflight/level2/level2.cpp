#include <iostream>
#include <fstream>
#include <string>
#include <algorithm> 
using namespace std;

int main() {
    ifstream file("level2_5.in");
    ofstream fileout("level25answer.in");

    int N;
    file >> N; 

    for (int path = 0; path < N; ++path) {
        string line;
        file >> line; 

        int height = 0, width = 0;
        int min_height = 0, max_height = 0;
        int min_width = 0, max_width = 0;

        for (char c : line) {
            switch (c) {
                case 'W': height--; break;
                case 'S': height++; break;
                case 'A': width--; break;
                case 'D': width++; break;
            }
            min_height = min(min_height, height);
            max_height = max(max_height, height);
            min_width = min(min_width, width);
            max_width = max(max_width, width);
        }

        int rect_height = max_height - min_height + 1;
        int rect_width = max_width - min_width + 1;

        fileout << rect_width << " " << rect_height << '\n';
    }

    file.close();
    fileout.close();
    return 0;
}
