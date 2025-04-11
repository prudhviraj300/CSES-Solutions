#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    long long sum = ((long long)n * (n+1)) / 2;
    
    for(int i = 1; i < n; i++){
        long long k;
        cin >> k;
        sum -= k;
    }
    cout << sum << endl;
    return 0;
}