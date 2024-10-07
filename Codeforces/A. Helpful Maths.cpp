#include <iostream>  
#include <string>
#include <vector>  

using namespace std;

int main(int argc, char* argv[]) {
    string s;
    cin >> s;

    vector<int> numbers;

    for (int i = 0; i < s.size(); i += 2) {
        numbers.push_back(s[i] - '0');
    }

    int n = numbers.size();
    for (int i = 1; i < n; ++i) {
        int key = numbers[i];
        int j = i - 1;

        while (j >= 0 && numbers[j] > key) {
            numbers[j + 1] = numbers[j];
            j = j - 1;
        }
        numbers[j + 1] = key;
    }
    
    for (int i = 0; i < n; ++i) {
        if (i > 0) cout << "+";
        cout << numbers[i];
    }
    cout << endl;

    return 0;
}