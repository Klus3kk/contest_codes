#include <iostream>  
#include <string>
#include <vector>  

using namespace std;

int main(int argc, char* argv[]) {
    string word;
    cin >> word;
    
    if(word[0] >= 'a' && word[0] <= 'z') {
        word[0] = word[0] - ('a' - 'A');
    }

    cout << word << endl;
    return 0;
}