#include<bits/stdc++.h>
using namespace std;


int main(){
    string str;
    cin >> str;
    int n = str.length();
    int ans = 0, cur = 0;
    char ch = str[0];
    for(int i = 0; i < n; i++){
        if(ch == str[i]){
            cur++;
        }else{
            cur = 1;
        }
        ch = str[i];
        ans = max(ans, cur);
    }
    cout << ans << endl;
    return 0;
}