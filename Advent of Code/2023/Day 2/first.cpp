#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdio>
#include <limits>

std::vector<std::string> processInput()
{
    std::string s;
    std::vector<std::string> input;
    while(std::getline(std::cin, s))
    {
        input.push_back(s);
    }
    return input;
}

long long part1(std::vector<std::string> input)
{
    long long sum = 0;
    for( auto &game : input)
    {
        game += ';';
        std::stringstream ss (game);

        std::string command;

        long long i = 0;

        long long red = 0;
        long long blue = 0;
        long long green = 0;

        long long number = 0;

        long long id = 0;

        bool is_possible = true;

        while(ss >> command)
        {
            ++i;

            if(i == 1) continue;

            if(i == 2)
            {
                command.pop_back();
                id = std::stol(command);
                continue;
            }

            if(command[0] >= '0' && command[0] <= '9')
            {
                number = std::stol(command);
            }
            else
            {

                if(command.find("red") != std::string::npos)
                {
                    red = number;
                    number = 0;
                }
                if(command.find("blue") != std::string::npos)
                {
                    blue = number;
                    number = 0;
                }
                if(command.find("green") != std::string::npos)
                {
                    green = number;
                    number = 0;
                }
                if(command[command.size() - 1] ==  ';')
                {
                    if(red > 12 || blue > 13 || green > 14) is_possible = false;

                    red = 0;
                    blue = 0;
                    green = 0;

                }
            }
        }
        if(is_possible)
        {
            sum += id;
        }
    }
    return sum;
}
int main()
{
    //std::freopen("day2inp.txt", "r", stdin);
    //std::freopen("day2out.txt", "w", stdout);

    std::vector<std::string> input = processInput();

    std::cout << "The solution for part 1 is: " << part1(input) <<'\n';

}
