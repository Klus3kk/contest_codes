#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

bool isValidMove(const vector<string>& lawn, int x, int y) {
    return (x >= 0 && x < lawn[0].size() && y >= 0 && y < lawn.size() && lawn[y][x] != 'X');
}

bool isPathValid(const vector<string>& lawn, const string& path, int startX, int startY) {
    vector<vector<bool>> visited(lawn.size(), vector<bool>(lawn[0].size(), false));
    queue<pair<int, int>> q;
    q.push({startX, startY});

    visited[startY][startX] = true;

    for (char dir : path) {
        int dx = 0, dy = 0;
        if (dir == 'W') dy = -1;
        else if (dir == 'A') dx = -1;
        else if (dir == 'S') dy = 1;
        else if (dir == 'D') dx = 1;

        int newX = q.back().first + dx;
        int newY = q.back().second + dy;
        if (!isValidMove(lawn, newX, newY) || visited[newY][newX]) {
            return false; 
        }
        q.push({newX, newY});
        visited[newY][newX] = true;
    }

    for (int i = 0; i < lawn.size(); ++i) {
        for (int j = 0; j < lawn[i].size(); ++j) {
            if (lawn[i][j] == '.' && !visited[i][j]) {
                return false; 
            }
        }
    }

    return true;
}

int main() {
    ifstream file("level3_example.in");
    ofstream fileout("level31answer.in");


    int N;
    file >> N;
    file.ignore(); 

    for (int i = 0; i < N; ++i) {
        int width, height;
        file >> width >> height;
        file.ignore(); 

        vector<string> lawn(height);
        for (int j = 0; j < height; ++j) {
            getline(file, lawn[j]);
        }

        string path;
        getline(file, path);

        bool valid = false;

        for (int startX = 0; startX < width; ++startX) {
            for (int startY = 0; startY < height; ++startY) {
                if (lawn[startY][startX] == '.') {
                    valid = isPathValid(lawn, path, startX, startY);
                    if (valid) break;
                }
            }
            if (valid) break;
        }

        fileout << (valid ? "VALID" : "INVALID") << '\n';
    }

    file.close();
    fileout.close();
    return 0;
}
