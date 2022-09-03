#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N, M;

int main(){

    cin >> N >> M;
    vector<int> vec(N);
    for (int i=0; i <N; i++){
        cin >> vec.at(i);
    }

    int cur_max = -100000000;
    for (int j=0; j<=N-M; j++){
        int total = 0;
        for (int k=0; k<M; k++){
            total += (k+1) * vec[j+k];
        }
        cur_max = max(cur_max, total);
    }
    cout << cur_max << endl;

    return 0;
}