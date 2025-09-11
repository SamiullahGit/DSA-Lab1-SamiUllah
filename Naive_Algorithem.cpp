#include <iostream>
#include <string>
using namespace std;
int findPattern(string text, string pattern) {
    
    if (pattern.empty()) {
        return -1;
    }

    for (int i = 0; i <= text.length() - pattern.length(); i++) {
        bool match = true;

        // Check each character of the pattern
        for (int j = 0; j < pattern.length(); j++) {
            if (text[i + j] != pattern[j]) {
                match = false;
                break;  
            }
        }

        if (match) {
            return i;
        }
    }

   // Pattern was not found
    return -1;
}

int main() {
    // Test Case 1: Pattern at the beginning
    string text1 = "hello My name is Sami Ullah";
    string pattern1 = "hello";
    cout << "Test Case 1 (Pattern at beginning): Index = " 
         << findPattern(text1, pattern1) << endl;

    // Test Case 2: Pattern at the end
    string text2 = "this is cpp";
    string pattern2 = "cpp";
    cout << "Test Case 2 (Pattern at end): Index = " 
         << findPattern(text2, pattern2) << endl;

    // Test Case 3: Pattern not present
    string text3 = "this is dsa lab";
    string pattern3 = "hello";
    cout << "Test Case 3 (Pattern not present): Index = " 
         << findPattern(text3, pattern3) << endl;

    // Test Case 4: Empty pattern
    string text4 = "random text";
    string pattern4 = "";
    cout << "Test Case 4 (Empty pattern): Index = " 
         << findPattern(text4, pattern4) << endl;

    return 0;
}
