#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <cstdio>

using namespace std;

int main()
{
    ifstream file("input.txt");

    char _;
    int no, idx = 0, sum = 0;
    vector<int> cards(199, 1);
    for (string line, card; getline(file, line); ++idx)
    {
        stringstream ss(line);
        ss >> card >> no >> _;
        vector<int> win_n = {istream_iterator<int>(ss), {}};
        ss = stringstream({line.begin() + (int)line.find('|') + 1, line.end()});
        vector<int> nums = {istream_iterator<int>(ss), {}};
        sort(win_n.begin(), win_n.end());

        int points = 0, won = 0;
        for (const auto n : nums)
        {
            if (binary_search(win_n.begin(), win_n.end(), n))
            {
                points = points ? points * 2 : 1;
                won++;
            }
        }

        for (size_t i = 0; i < cards[idx]; ++i)
        {
            int t_idx = idx;
            for (size_t i = 0; i < won; ++i)
                cards[++t_idx]++;
        }

        sum += points;
    }
    auto sum2 = accumulate(cards.begin(), cards.end(), 0);

    printf("part1: %d\n", sum);
    printf("part2: %d\n", sum2);
    return 0;
}
