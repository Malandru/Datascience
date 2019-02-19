#include <iostream>
#include <regex>
using namespace std;

char *arg; string line;
int indx, len;
int matches, lines;

void readfile();
bool analize(string, int);
void mvnextln();
bool is_endl(char);
void update();

int length_of(char *str)
{
    int len;
    while(*(str++) != '\0') len++;
    return len;
}

int main(int argc, char **argv)
{
    arg = argv[1];
    len = length_of(arg);
    readfile();
    printf("%d matches of %d lines\n", matches, lines);
    return 0;
}

void readfile()
{
    char read; line = "";
    string word = "";
    while(true)
    {
        read = getchar();
        if(read == ',')
        {
            line += word + char(92);
            if(analize(word, indx++))
                mvnextln();
            word = "";
        }
        else if(is_endl(read))
        {
            line += word;
            // cout << "[" << word << "]\n";
            if(analize(word, indx++));
            else if(indx < len);
            else
            {
                cout << line << endl;
                matches++;
            }
            word = "";
            update();
            if(read == EOF)
                break;
        }
        else
            word += read;
    }
}

bool analize(string word, int p)
{
    // cout << "Analizing [" << word << "] Index: [" <<  p <<  "]";
    if(p >= len)
        return true;
    regex _regex("[+-]?[0-9]+([.][0-9]+)?([eE][+-]?[0-9]+)?");
    bool isnumber = regex_match(word, _regex);
    // cout << " es numero: [" << isnumber << "]" << endl;
    if(isnumber and arg[p] == 'n') return false;
    if(!isnumber and arg[p] == 'c') return false;
    return true;
    //mvnextln();
}

void mvnextln()
{
    while(!is_endl(getchar()));
    update();
}

bool is_endl(char read)
{
    return read == 10 ||
           read == 13 ||
           read == EOF;
}

void update()
{
    getchar();
    lines++;
    indx = 0;
    line = "";
}