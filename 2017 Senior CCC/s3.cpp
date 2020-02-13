#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int count;
    int freq[4001] = {};

    cin>>count;
    for (int i = 0; i < count; i++){
        int spot;
        cin>>spot;
        freq[spot]++;
    }

    int sums[4001] = {};
    for (int wantedSum = 1; wantedSum < 4001; wantedSum++){
        for (int num1 = 1; num1 <= wantedSum/2; num1++){
            if (num1 == wantedSum - num1){ // stack itself
                sums[wantedSum] += (int) (freq[num1]/2);
            }else{ // stack with other end
                int nums = min(freq[num1], freq[wantedSum - num1]);
                sums[wantedSum] += nums;
            }
        }
    }

    int largestCount = -1;
    int occur = 0;

    for (int i = 0; i<4001; i++){
        if (sums[i] > largestCount){
            largestCount = sums[i];
            occur = 1;
        }else if (sums[i] == largestCount){
            occur++;
        }
    }

    cout<< largestCount << " " << occur << endl;
    return 0;
}