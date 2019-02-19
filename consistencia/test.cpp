#include <iostream>
#include <cstdio>
#include <regex>
using namespace std;

string get_regex(char *arg)
{
    string _regex = "";
    int i = 0; char c;
    while((c = arg[i++]) != '\0')
    {
        if(c == 'c') _regex += "[a-zA-Z ]+|";
        else if(c == 'n') _regex += "[0-9]+|[0-9]+[.][0-9]+";
        
        if(arg[i] != '\0')
            _regex += ",";
    }
    return _regex;
}

int main(int argc, char **argv)
{
    int matches = 0, lines = 0;
    cout << get_regex(argv[1]) << endl;
    regex _regex (get_regex(argv[1]));
    char input[255];
    while(fgets(input, sizeof(input), stdin))
    {
        input[strcspn(input, "\n")] = 0;
        if(regex_match(input, _regex))
            matches++;
        lines++;
    }
    float p = float(matches * 100) / lines;
    printf("%d lines of %d (%f%c)\n", matches, lines, p, 37);
    return 0;
}