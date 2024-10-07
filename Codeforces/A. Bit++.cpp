#include <iostream>      
#include <cstdio>        
#include <iomanip>  
#include <vector>        // Dynamic arrays
#include <deque>         // Double-ended queue
#include <queue>         // Queue, priority queue
#include <stack>         // Stack
#include <set>           // Set for unique elements (sorted)
#include <map>           // Map for key-value pairs
#include <unordered_map> // Hash map for key-value pairs (unordered)
#include <unordered_set>
#include <algorithm>     // Sorting, searching, min/max, etc.
#include <numeric>       // Operations like accumulate, partial_sum
#include <string>        // String class and related functions
#include <sstream>       // String stream for parsing/formatting
#include <utility>       // For pairs, swap, etc.
#include <tuple>         // For handling tuples
#include <bitset>        // For bit manipulation (useful in combinatorics)
#include <cstdlib>       // C-style random numbers (rand(), srand())
#include <ctime>         // Time for seeding random number generator

using namespace std;

int main(int argc, char* argv[]) {
    int n;
    cin >> n;

    int x = 0;

    for (int i = 0; i < n; ++i) {
        string statement;
        cin >> statement;

        if (statement.find("++") != string::npos) {
            ++x;
        } else if (statement.find("--") != string::npos) {
            --x;
        }
    }

    cout << x << endl;
    return 0;
}