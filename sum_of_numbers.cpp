#include <vector>
#include <iostream>

using namespace std;

int how_many_ways_to_sum(int n) {
    // The function works by first generating a partition table as a vector, which it then later iterates over.
    // The idea is that each element n in the table can be represented as the sum of the previous elements. For example,
    // 5 = 1 + 1 + 1 + 1 + 1. This can be then split into different parts: 5 = (1 + 1) + (1 + 1) + 1 = 2 + 2 + 1. If we would have looked for all the ways a number can
    // be represented as a sum of smaller numbers, this would have left us with 2 ^ (n - 1) different combinations. However in this case the order matters- we don't want
    // to consider 5 = 2 + 2 + 1 and 5 = 1 + 2 + 2 as different. 

    // When I was coding the task, I have to admit that I got a bit lost with the aforementioned, trying to find a relationship between the 2 ^ (n - 1) and the actual
    // number. However, I realized that for each N, we can use the previous elements- as 5 can be written as 3 + 2, and we already know that
    // 3 and 2 can be written as 2 + 1 or 1 + 1 + 1 and 1 + 1 respectively. Thus we know that for 5, we have from 3 and 2 already 3 ways of writing it.
    // Using this knowledge, we can efficiently move through the whole list.
    vector<int> summed_numbers(n+1, 0);

    summed_numbers[0] = 1; // only one way to make 1

    for (int i = 1; i < n; i++) {
        for (int j = i; j <= n + 1; j++) {
            summed_numbers[j] += summed_numbers[j - i]; // Each number has the as many ways to make it as is the sum of the ways for previous numbers. 1 way to make two, 2 ways to make 3, 4 ways to make 4 etc.
        }
    }

    return summed_numbers[n]; // Return the n:th element
}

void main() {
    int n = 100;
    cout << how_many_ways_to_sum(n) << endl;
}