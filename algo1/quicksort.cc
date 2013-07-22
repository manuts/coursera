/*
Copyright 2013 IIT Bombay.
Author: Manu T S

This is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3, or (at your option)
any later version.

This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this software; see the file COPYING.  If not, write to
the Free Software Foundation, Inc., 51 Franklin Street,
Boston, MA 02110-1301, USA.
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

void median(vector<int> &A, int l, int r) {
    int start = A[l];
    int mid = A[l + (r -l)/2];
    int end = A[r];
    if (((start <= mid) && (mid <= end)) ||((end <= mid) && (mid <= start))){
        A[l] = mid;
        A[l + (r-l)/2] = start;
    }
    else if (((mid <= end) && ( end <= start)) || ((start <= end) && (end <= mid))){
        A[l] = end;
        A[r] = start;
    }
}

int partition(vector<int> &A, int l, int r, int & count) {
    count += r - l;
    median(A, l, r);
    int pivot = A[l];
    int i = l + 1;
    for (int j = l + 1; j <= r; j++) {
        if (A[j] < pivot) {
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            i++;
        }
    }
    A[l] = A[i - 1];
    A[i - 1] = pivot;
    return i - 1;
}

void quicksort(vector<int> &A, int l, int r, int & count) {
    if (r - l < 1) {
        return;
    }
    int k = partition(A, l, r, count);
    quicksort(A, l, k - 1, count);
    quicksort(A, k + 1, r, count);
}

int main() {
    vector<int> A;
    int count = 0;
    A.resize(10000);
    ifstream file;
    string line;
    stringstream ss;
    file.open("QuickSort.txt");
    for ( int i = 0; i < 10000; i++) {
        getline(file, line);
        ss << line;
        ss >> A[i];
    }
    quicksort(A, 0, 9999, count);
    bool order = true;
    for ( int i = 0; i < 10000; i++){
        if (A[i] != i + 1) {
            order = false;
        }
    }
    if (order) {
        cout << "order" << '\n';
    }
    cout << count << '\n';
}
