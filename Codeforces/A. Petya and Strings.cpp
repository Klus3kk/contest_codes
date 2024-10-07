#include <iostream>  

using namespace std;

int main(int argc, char* argv[]) {
    string word1, word2;

    cin >> word1 >> word2;

    for(int i = 0; i < word1.length(); i++) {
        char char1 = tolower(word1[i]);
        char char2 = tolower(word2[i]);

        if(char1 < char2) {
            cout << -1 << endl;
            return 0;
        } else if (char1 > char2) {
            cout << 1 << endl;
            return 0;
        }
    }

    cout << 0 << endl;
    return 0;
}