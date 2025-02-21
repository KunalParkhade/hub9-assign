#include <bits/stdc++.h>
using namespace std;

void sort(int width, int height, int length, int mass)
{
    long long int total = width * height * length;
    if ((total >= 1000000) || (width >= 150) || (height >= 150) || (length >= 150))
    {
        if (mass >= 20)
        {
            cout << "REJECTED";
        }
        else
        {
            cout << "SPECIAL";
        }
    }
    else if (mass >= 20)
    {
        cout << "SPECIAL";
    }
    else
    {
        cout << "STANDARD";
    }
}

int main()
{
    int width, height, length;
    int mass;
    cin >> width >> height >> length >> mass;

    sort(width, height, length, mass);

    return 0;
}