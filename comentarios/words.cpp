#include <iostream>
using namespace std;

bool newline(char);
void read_commentary(bool&);

int main()
{
    char buffer[512];
    bool keep_reading = true;
    // fgets(buffer, sizeof(buffer), stdin);
    // printf("%s", buffer);
    while(keep_reading)
    {
        fgets(buffer, sizeof(buffer), stdin);
        // printf("%s", buffer); //Prints the whole line of csv
        read_commentary(keep_reading);
    }
    return 0;
}

bool newline(char c)
{
    return c == 10 ||
           c == 13 ||
           c == EOF;
}

void read_commentary(bool &keep_reading)
{
    string word = "";
    char c;
    while (!newline(c = getchar()))
        if(isalpha(c) or isdigit(c) or isspace(c))
            word += c;
    cout << word << endl;
    keep_reading = (c != EOF);
}