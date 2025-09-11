#include <iostream>
#include <vector>
using namespace std;

// Declaring the function to find the indices
vector<int> findAllIndices(int arr[], int size, int key) {
    vector<int> indices;  

    for (int i = 0; i < size; i++) {
        if (arr[i] == key) {
            indices.push_back(i);  
        }
    }
    return indices;  
}
 //This is a new comment
int main() {

    // Test Case 1: Multiple occurrences
    int arr1[] = {1, 3, 5, 3, 7, 3, 9};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int key1 = 3;

    vector<int> result1 = findAllIndices(arr1, size1, key1);
    cout << "Test Case 1 (key appears multiple times): ";
    if (result1.empty()) {
        cout << "Key not found.";
    } else {
        for (int index : result1) {
            cout << index << " ";
        }
    }
    cout << endl;

    // Test Case 2: Key not present
    
    int arr2[] = {2, 4, 6, 8};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    int key2 = 5;

    vector<int> result2 = findAllIndices(arr2, size2, key2);
    cout << "Test Case 2 (key not present): ";
    if (result2.empty()) {
        cout << "Key not found.";
    } else {
        for (int index : result2) {
            cout << index << " ";
        }
    }
    cout << endl;

    // Test Case 3: Empty array
    
    int arr3[] = {};  // no elements
    int size3 = 0;
    int key3 = 10;

    vector<int> result3 = findAllIndices(arr3, size3, key3);
    cout << "Test Case 3 (empty array): ";
    if (result3.empty()) {
        cout << "Array is empty or key not found.";
    } else {
        for (int index : result3) {
            cout << index << " ";
        }
    }
    cout << endl;

    return 0;
}
