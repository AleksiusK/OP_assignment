#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

// The problem consists of two parts: firts, split the number into digits (done in thes
// split_number function) and then checking the "bounciness" of the number. We could use the
// information that bouncy number frequency is 90% exact when we reach 21780, but that feels like cheating.

// The bounciness is checked by first inspecting the order of elements- normal and reversed- and from there calculating the frequency.
// When checking the bounciness, we could also use a an approach that would eliminate the flipped numbers,
// e.g when checking 123 for bounciness, we would also eliminate 321 at the ame time.
// However, this is not really required and would add only a small boost to the efficiency, as the number of
// bouncy numbers gets larger the bigger range_n we use. At some point, we would need to check almost all numbers.

// The complexity of the function is O(range_n), as we need to loop through the whole list of numbers. In addition, the split_number function
// increases the complexity by the average of the lenght of numbers.


vector<int> split_number(int number) {
    int num = number;
    vector<int> digits;
    while (num > 0) {
        int digit = num % 10; // Get the last digit
        num /= 10; // Remove the last digit
        digits.push_back(digit);
    }
    return digits;
}

double bouncy_numbers(int range_n) {
    int bouncy = 0;
    double frequency = 0.0;
    for (int i = 100; i <= range_n; i++) {
        vector<int> digits = split_number(i);
        if (is_sorted(digits.begin(), digits.end())) {
            continue; // If the number is sorted smallest - largest, skip the rest
        }
        reverse(digits.begin(), digits.end()); // Flip the vector
        if (is_sorted(digits.begin(), digits.end())) {
            continue;  // Run the same check again. If the number is sorted largest - smallest, skip the rest
        }
        else {
            bouncy++; // If the number is not sorted in either direction, it is bouncy
            frequency = ceil(((double)bouncy / (double)i) * 100) / 100.0; // Calculate the frequency to two digit precision
            // Exit if the frequency is 99% exact
            if (frequency == 0.99) {
                cout << "Frequency exactly 99%. Number: " << i << endl;
                break;
            }
        }
    }
    cout << "Bouncy numbers below the given range: " << bouncy << endl;
    return frequency;
}


void main () {
    int range_n = 1000000;
    cout << "Frequency of bouncy numbers: " << bouncy_numbers(range_n) << endl;
}
