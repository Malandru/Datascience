#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void to_date(time_t seconds)
{
    char buffer[80];
    struct tm *date;
    date = gmtime(&seconds);
    strftime(buffer, sizeof(buffer), "%c", date);
    printf("%ld seconds = %s\n", seconds, buffer);
}

time_t to_seconds(struct tm date)
{
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%c", &date);
    time_t seconds = timegm(&date);
    // printf("%s = %ld seconds:\n", buffer, seconds);
    return seconds;
}

int read_num(char *buffer)
{
    scanf("%s", buffer);
    return atoi(buffer);
}

struct tm read_date()
{
    struct tm date;
    char buffer[8];
    date.tm_year = read_num(buffer) - 1900;
    date.tm_mon = read_num(buffer) - 1;
    date.tm_mday = read_num(buffer);
    date.tm_hour = read_num(buffer);
    date.tm_min = read_num(buffer);
    date.tm_sec = read_num(buffer);
    date.tm_isdst = -1;
    return date;
}

int main()
{
    // time_t to_now;
    // to_now = time(NULL);
    // printf("Seconds to now: %ld\n", to_now);
    // to_date(to_now);
    char buffer[127];
    fgets(buffer, sizeof(buffer), stdin);
    printf("%s", buffer);

    struct tm date; float amount;
    while(1)
    {
        date = read_date();
        if(date.tm_year < 0)
            break;

        time_t pickup = to_seconds(date);
        time_t dropoff = to_seconds(read_date());
        time_t diff = dropoff - pickup;

        scanf("%f", &amount);

        if(diff > 0 && diff < 43200 && amount > 0 && amount < 1500)
            printf("%ld,%f\n", diff, amount);
    }

    // to_date(pickup);
    // to_date(dropoff);
    
    // ret = timegm(&info);
    // printf("My date: %ld\n", ret);
    // ret = mktime(&info);
    // printf("Con mkt: %ld\n", ret);
    return 0;
}