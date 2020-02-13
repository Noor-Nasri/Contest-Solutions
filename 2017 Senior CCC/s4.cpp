#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int buildings, pipes, enhancer;
    cin >> buildings >> pipes >> enhancer;

    int perfectPipes[200000] = {};
    int startingPipes[200000] = {};
    vector<int[3]> Pathways[100000] = {};

    for (int i = 0; i < pipes; i++){
        int start, end, cost;
        cin >> start >> end >> cost;
        start--;
        end--;

        int forstart[3] = {end, cost, i};
        Pathways[start].push_back(forstart); 
        
        int forend[3] = {start, cost, i};
        Pathways[end].push_back(forend); 

        if (i < buildings - 1){ // starting pipes
            startingPipes[i] = true;
        }
    }

    // dijsktras now
    int shortestPaths[100000] = {};
    vector<int[2]> queue(1); // [current pos, cost so far]

    while (true){
        int minValue = -1;
        int headingTo = -1;
        int pipeIndex = -1;

        for (int currentSpot = 0; currentSpot < queue.size(); currentSpot++){
            
        }


        if (headingTo == -1){
            break;
        }
    }

    int diff = 0;
    for (int c = 0; c < 200000; c++){
        if (perfectPipes[c] != startingPipes[c]){
            diff++;
        }
    }

    cout<<diff<<endl;

    return 0;
}
