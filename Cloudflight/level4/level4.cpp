#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

bool isValidMove(const vector<string>& lawn, const Point& p, const Point& tree) {
    return p.x >= 0 && p.x < lawn[0].size() && p.y >= 0 && p.y < lawn.size() &&
           lawn[p.y][p.x] == '.' && !(p.x == tree.x && p.y == tree.y);
}

int countUnvisitedNeighbors(const Point& pos, const vector<vector<bool>>& visited, const vector<string>& lawn) {
    int count = 0;
    const vector<Point> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (const auto& dir : directions) {
        Point neighbor = {pos.x + dir.x, pos.y + dir.y};
        if (neighbor.x >= 0 && neighbor.x < visited[0].size() && neighbor.y >= 0 && neighbor.y < visited.size()) {
            if (!visited[neighbor.y][neighbor.x] && lawn[neighbor.y][neighbor.x] == '.') {
                count++;
            }
        }
    }
    return count;
}

bool isComplete(const vector<vector<bool>>& visited, int freeSpots) {
    int count = 0;
    for (const auto& row : visited) {
        for (bool v : row) {
            if (v) ++count;
        }
    }
    return count == freeSpots;
}

bool isValidPrune(const vector<string>& lawn, const vector<vector<bool>>& visited, const Point& nextPos) {
    vector<vector<bool>> tempVisited = visited;
    tempVisited[nextPos.y][nextPos.x] = true;

    return true;
}



bool generatePath(vector<string>& lawn, Point pos, string& path, vector<vector<bool>>& visited, const Point& tree, int freeSpots) {
    if (isComplete(visited, freeSpots)) {
        cout << "Found valid path: " << path << endl;
        return true;
    }

    vector<pair<Point, int>> moves = {{{-1, 0}, 0}, {{1, 0}, 0}, {{0, -1}, 0}, {{0, 1}, 0}}; 
    const string directions = "UDLR";

    for (auto& move : moves) {
        Point nextPos = {pos.x + move.first.x, pos.y + move.first.y};
        if (isValidMove(lawn, nextPos, tree) && !visited[nextPos.y][nextPos.x]) {
            move.second = -countUnvisitedNeighbors(nextPos, visited, lawn);
        } else {
            move.second = INT_MIN; 
        }
    }

    sort(moves.begin(), moves.end(), [](const pair<Point, int>& a, const pair<Point, int>& b) {
        return a.second > b.second;
    });

    for (const auto& move : moves) {
        if (move.second == INT_MIN) continue; 

        Point nextPos = {pos.x + move.first.x, pos.y + move.first.y};
        path.push_back(directions[&move - &moves[0]]);
        visited[nextPos.y][nextPos.x] = true;

        if (isValidPrune(lawn, visited, nextPos) && generatePath(lawn, nextPos, path, visited, tree, freeSpots)) {
            return true;
        }

        visited[nextPos.y][nextPos.x] = false;
        path.pop_back();
    }

    return false;
}

int main() {
    ifstream file("level4_example.in");
    ofstream fileout("level4_example.out");

    int N;
    file >> N;

    for (int i = 0; i < N; ++i) {
        int width, height;
        file >> width >> height;

        vector<string> lawn(height);
        Point startPos;
        Point tree;
        int freeSpots = 0;
        vector<vector<bool>> visited(height, vector<bool>(width, false));

        for (int j = 0; j < height; ++j) {
            file >> lawn[j];
            for (int k = 0; k < width; ++k) {
                if (lawn[j][k] == '.') {
                    freeSpots++;
                    if (startPos.x == -1 && startPos.y == -1) {
                        startPos = {k, j};
                    }
                } else if (lawn[j][k] == 'T') {
                    tree = {k, j};
                }
            }
        }

        visited[startPos.y][startPos.x] = true; 
        string path;
        bool found = generatePath(lawn, startPos, path, visited, tree, freeSpots);
        if (found) {
            fileout << path << '\n';
        } else {
            fileout << "No valid path found" << '\n';
        }
    }

    file.close();
    fileout.close();
    return 0;
}