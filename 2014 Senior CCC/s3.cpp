#include <iostream>
using namespace std;

int main(){
    int num_cases;
    cin>>num_cases;
    
    for (int i = 0; i < num_cases; i++){
        int num_numbers;
        cin >> num_numbers;
        
        int numbers[100000] = {};
        int branch[100000 * 2] = {};
        for (int a = 1; a<=num_numbers; a++){
            cin >> numbers[num_numbers - a];
        }

        int wantedNumber = 1;
        int currentIndex = 0;
        int branchIndex = 100000;
        while (currentIndex < num_numbers){
            if (numbers[currentIndex] == wantedNumber){
                wantedNumber++;
                currentIndex++;
            }else if (branch[branchIndex] == wantedNumber){
                wantedNumber++;
                branch[branchIndex] = 0;
                branchIndex--;
            }else{ // move one over
                branchIndex++;
                branch[branchIndex] = numbers[currentIndex];
                currentIndex++;
            }

            if (currentIndex == num_numbers){ // time to wrap up
                for (int b = branchIndex + 1; b--; b>=0){
                    if (branch[b] != wantedNumber){
                        break;
                    }else {
                        wantedNumber++;
                    }
                }
            }
        }

        cout << ((wantedNumber > num_numbers) ?  "Y" : "N") << endl;

    }

    return 0;
}